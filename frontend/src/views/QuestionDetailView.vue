<template>
  <div class="question-detail">
    <h1 class="text-3xl font-bold mb-6">{{ question.title }}</h1>
    <div class="bg-white shadow-md rounded-lg p-4 mb-6">
      <p class="text-gray-800">{{ question.text }}</p>
      <div class="flex items-center mt-2 text-sm text-gray-500">
        <span>{{ question.user_name }}</span>
        <span class="mx-2">•</span>
        <span>{{ formatDate(question.creation_time) }}</span>
      </div>
      <div v-if="question.category_name" class="mt-4">
        <strong>Категория:</strong>
        <span class="bg-green-200 text-green-800 px-3 py-1 rounded-full ml-2">
          {{ question.category_name }}
        </span>
      </div>
      <div v-if="question.tag_names && question.tag_names.length" class="mt-4">
        <strong>Теги:</strong>
        <span
          v-for="tag in question.tag_names"
          :key="tag"
          class="bg-blue-200 text-blue-800 px-3 py-1 rounded-full ml-2"
        >
          {{ tag }}
        </span>
      </div>
    </div>

    <div v-if="isAuthenticated" class="mb-8">
      <h3 class="text-xl font-bold mb-4">Ваш ответ</h3>
      <form @submit.prevent="submitAnswer" class="space-y-4">
        <textarea
          v-model="newAnswer"
          required
          placeholder="Напишите ваш ответ..."
          class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
        />
        <button
          type="submit"
          class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Отправить ответ
        </button>
      </form>
    </div>

    <h2 class="text-2xl font-bold mb-4">Ответы</h2>
    <ul class="space-y-4">
      <li v-for="answer in answers" :key="answer.id" class="bg-white shadow-md rounded-lg p-4">
        <p class="text-gray-800">{{ answer.text }}</p>
        <div class="flex items-center mt-2 text-sm text-gray-500">
          <span>{{ answer.user_name }}</span>
          <span class="mx-2">•</span>
          <span>{{ formatDate(answer.creation_time) }}</span>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import { fetchQuestionById, fetchAnswersByQuestionId, createAnswer } from '@/services/forumApi';

export default {
  setup() {
    const store = useStore();
    const route = useRoute();
    const question = ref({ tag_names: [], category_name: '' });
    const answers = ref([]);
    const newAnswer = ref('');

    const isAuthenticated = computed(() => store.getters.isAuthenticated);

    const loadQuestionAndAnswers = async () => {
      try {
        const questionData = await fetchQuestionById(route.params.id);
        question.value = questionData;
        answers.value = await fetchAnswersByQuestionId(route.params.id);
      } catch (error) {
        console.error('Ошибка при загрузке данных:', error);
        alert('Не удалось загрузить вопрос или ответы.');
      }
    };

    const submitAnswer = async () => {
      try {
        await createAnswer({
          question_id: parseInt(route.params.id),
          text: newAnswer.value,
        });
        newAnswer.value = '';
        await loadQuestionAndAnswers();
      } catch (error) {
        console.error('Ошибка при отправке ответа:', error);
        alert('Не удалось отправить ответ. Попробуйте снова.');
      }
    };

    onMounted(() => {
      loadQuestionAndAnswers();
    });

    return {
      question,
      answers,
      newAnswer,
      isAuthenticated,
      submitAnswer,
      formatDate: (date) => new Date(date).toLocaleDateString(),
    };
  },
};
</script>