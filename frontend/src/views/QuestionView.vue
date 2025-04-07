<template>
  <div class="question-detail max-w-3xl mx-auto p-6 bg-white shadow-md rounded-lg">
    <h1 class="text-3xl font-bold mb-4">{{ question.title }}</h1>
    <p class="text-gray-700 mb-4">{{ question.text }}</p>
    <div class="flex items-center text-sm text-gray-500 mb-6">
      <span>Автор: {{ question.user_name }}</span>
      <span class="mx-2">•</span>
      <span>{{ formatDate(question.creation_time) }}</span>
    </div>
    <div class="mb-6">
      <p><strong>Категория:</strong> {{ question.category_name }}</p>
      <p><strong>Теги:</strong> {{ question.tag_names.join(', ') }}</p>
    </div>

    <h2 class="text-2xl font-bold mb-4">Ответы</h2>
    <AnswerList :answers="answers" />

    <form @submit.prevent="submitAnswer" class="mt-6">
      <textarea
        v-model="newAnswer"
        placeholder="Напишите ваш ответ"
        class="w-full h-32 p-2 border border-gray-300 rounded resize-none focus:outline-none focus:ring-2 focus:ring-blue-500"
      ></textarea>
      <button type="submit" class="btn">Отправить</button>
    </form>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { fetchQuestionById, fetchAnswersByQuestion } from '@/services/forumApi';

export default {
  name: 'QuestionView',
  setup() {
    const route = useRoute();
    const questionId = route.params.id;
    const question = ref({});
    const answers = ref([]);
    const newAnswer = ref('');

    onMounted(async () => {
      question.value = await fetchQuestionById(questionId);
      answers.value = await fetchAnswersByQuestion(questionId);
    });

    const submitAnswer = async () => {
      if (newAnswer.value.trim()) {
        console.log('Ответ отправлен:', newAnswer.value);
        answers.value.push({ content: newAnswer.value, author: 'Вы', createdAt: new Date() });
        newAnswer.value = '';
      }
    };

    const formatDate = (date) => {
      return new Date(date).toLocaleDateString();
    };

    return { question, answers, newAnswer, submitAnswer, formatDate };
  },
};
</script>