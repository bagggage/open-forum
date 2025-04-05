<template>
    <div class="question-detail">
      <div class="question-bar">
        <h1>{{ question.title }}</h1>
        <div class="flex items-center mb-4">
          <span>{{ question.user_name }}</span>
          <span class="mx-2">•</span>
          <span>{{ formatDate(question.creation_time) }}</span>
        </div>
      </div>
      <p>{{ question.text }}</p>
      <hr/>
      <h2>Ответы</h2>
      <ul class="space-y-4">
        <li v-for="answer in answers" :key="answer.id" class="bg-white shadow-md rounded-lg p-4">
          <p>{{ answer.text }}</p>
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
      const question = ref({ tag_names: [] });
      const answers = ref([]);
  
      const loadQuestionAndAnswers = async () => {
        try {
          const questionData = await fetchQuestionById(route.params.id);
          question.value = questionData;
          answers.value = await fetchAnswersByQuestionId(route.params.id);
        } catch (error) {
          console.error('Ошибка при загрузке вопроса:', error);
          alert('Не удалось загрузить вопрос.');
        }
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