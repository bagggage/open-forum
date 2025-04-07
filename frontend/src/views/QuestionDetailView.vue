<template>
    <div class="question-detail">
      <div class="question-bar">
        <h1 class="question-title">{{ question.title }}</h1>
        <div class="flex items-center mb-4">
          <span>{{ question.user_name }}</span>
          <span class="mx-2">•</span>
          <span>{{ formatDate(question.creation_time) }}</span>
        </div>
      </div>
      <p>{{ question.text }}</p>
      <hr/>
      <h2>Ответы</h2>

      <AnswerList :answers=answers />

      <!-- Форма ответа для авторизованных пользователей -->
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
            class="btn"
          >
            Отправить ответ
          </button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted, computed } from 'vue';
  import { useRoute } from 'vue-router';
  import { useStore } from 'vuex';
  import { fetchQuestionById, fetchAnswersByQuestionId, createAnswer } from '@/services/forumApi';
  import AnswerList from '@/components/AnswerList.vue'
  
  export default {
    components: { AnswerList },
    setup() {
      const store = useStore();
      const route = useRoute();
      const question = ref({ tag_names: [] });
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
          await loadQuestionAndAnswers(); // Обновляем список ответов
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