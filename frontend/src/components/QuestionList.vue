<template>
  <div>
    <ul v-if="filteredQuestions.length" class="space-y-4">
      <li v-for="question in filteredQuestions" :key="question.id">
        <QuestionPreview :question=question />
      </li>
    </ul>
    <p v-else>Нет вопросов, соответствующих вашему запросу.</p>

    <div class="pagination flex justify-between mt-6">
      <button
        @click="prevPage"
        :disabled="currentPage === 0"
        class="px-4 py-2 bg-gray-200 text-gray-700 rounded disabled:opacity-50"
      >
        Предыдущая
      </button>
      <span class="text-gray-700">Страница {{ currentPage + 1 }}</span>
      <button
        @click="nextPage"
        :disabled="!hasMorePages"
        class="px-4 py-2 bg-gray-200 text-gray-700 rounded hover:bg-gray-300 disabled:opacity-50"
      >
        Следующая
      </button>
    </div>
  </div>
</template>

<script>
import { ref, watch, onMounted, computed } from 'vue';
import { fetchQuestions, fetchQuestionsByCategory } from '@/services/forumApi';
import QuestionPreview from './QuestionPreview.vue';

export default {
  props: {
    categoryName: { type: String, default: '' },
    searchQuery: { type: String, default: '' },
    currentPage: { type: Number, default: 0 },
  },
  components: { QuestionPreview },
  emits: ['update-page'],
  setup(props, { emit }) {
    const questions = ref([]);
    const limit = 10;

    const loadQuestions = async () => {
      try {
        if (props.categoryName) {
          questions.value = await fetchQuestionsByCategory(
            props.categoryName,
            props.currentPage * limit,
            limit
          );
        } else {
          questions.value = await fetchQuestions(
            props.currentPage * limit,
            limit
          );
        }
      } catch (error) {
        console.error('Ошибка при загрузке вопросов:', error);
        questions.value = [];
      }
    };

    onMounted(() => {
      loadQuestions();
    });

    watch(
      () => [props.categoryName, props.currentPage],
      () => {
        loadQuestions();
      }
    );

    const filteredQuestions = computed(() => {
      if (!props.searchQuery) {
        return questions.value;
      }
      const query = props.searchQuery.toLowerCase();
      return questions.value.filter((question) =>
        question.title.toLowerCase().includes(query)
      );
    });

    const hasMorePages = computed(() => {
      return questions.value.length === limit;
    });

    const nextPage = () => {
      if (hasMorePages.value) {
        emit('update-page', props.currentPage + 1);
      }
    };

    const prevPage = () => {
      if (props.currentPage > 0) {
        emit('update-page', props.currentPage - 1);
      }
    };

    return { questions, filteredQuestions, nextPage, prevPage, hasMorePages };
  },
};
</script>