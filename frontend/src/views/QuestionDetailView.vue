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
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  import { fetchQuestionById, fetchAnswersByQuestionId } from '@/services/forumApi';
  
  export default {
    setup() {
      const route = useRoute();
      const question = ref({});
      const answers = ref([]);
  
      const loadQuestionAndAnswers = async () => {
        const questionId = parseInt(route.params.id);
        question.value = await fetchQuestionById(questionId);
        answers.value = await fetchAnswersByQuestionId(questionId);
      };
  
      const formatDate = (date) => {
        return new Date(date).toLocaleDateString();
      };
  
      onMounted(() => {
        loadQuestionAndAnswers();
      });
  
      return { question, answers, formatDate };
    },
  };
  </script>