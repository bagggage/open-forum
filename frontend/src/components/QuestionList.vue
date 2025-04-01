<template>
  <ul class="space-y-4">
    <li v-for="question in questions" :key="question.id" class="bg-white shadow-md rounded-lg p-4">
      <p class="text-xl font-semibold text-gray-800">{{ question.title }}</p>
      <p class="text-gray-600 mt-2">{{ truncateText(question.text, 100) }}</p>
      <div class="flex items-center mt-2 text-sm text-gray-500">
        <span>{{ question.user_name }}</span>
        <span class="mx-2">•</span>
        <span>{{ formatDate(question.creation_time) }}</span>
      </div>
    </li>
  </ul>
</template>

<script>
import { ref, onMounted } from 'vue';
import { fetchQuestions } from '@/services/forumApi';

export default {
  setup() {
    const questions = ref([]);

    onMounted(async () => {
      questions.value = await fetchQuestions(0, 10); // Загружаем первые 10 вопросов
    });

    const formatDate = (date) => {
      return new Date(date).toLocaleDateString();
    };

    const truncateText = (text, maxLength) => {
      if (text.length > maxLength) {
        return text.substring(0, maxLength) + '...';
      }
      return text;
    };

    return { questions, formatDate, truncateText };
  },
};
</script>