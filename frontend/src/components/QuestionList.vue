<template>
  <div>
    <ul v-if="questions.length" class="space-y-4">
      <li v-for="question in questions" :key="question.id" class="bg-white shadow-md rounded-lg p-4">
        <p class="text-xl font-semibold text-blue-600 hover:text-blue-800">
          {{ question.title }}
        </p>
        <div class="flex items-center mt-2 text-sm text-gray-500">
          <span>{{ question.user_name }}</span>
          <span class="mx-2">•</span>
          <span>{{ formatDate(question.creation_time) }}</span>
        </div>
      </li>
    </ul>
    <p v-else>Нет вопросов в этой категории.</p>
  </div>
</template>

<script>
import { ref, watch, onMounted } from 'vue';
import { fetchQuestions, fetchQuestionsByCategory } from '@/services/forumApi';

export default {
  props: {
    categoryName: {
      type: String,
      default: '',
    },
  },
  setup(props) {
    const questions = ref([]);

    const loadQuestions = async () => {
      try {
        if (props.categoryName) {
          questions.value = await fetchQuestionsByCategory(props.categoryName);
        } else {
          questions.value = await fetchQuestions(0, 10); // Загружаем последние 10 вопросов
        }
      } catch (error) {
        console.error('Ошибка при загрузке вопросов:', error);
        questions.value = []; // Очищаем список вопросов
      }
    };

    watch(
      () => props.categoryName,
      () => {
        loadQuestions();
      }
    );

    onMounted(() => {
      loadQuestions();
    });

    const formatDate = (date) => {
      return new Date(date).toLocaleDateString();
    };

    return { questions, formatDate };
  },
};
</script>