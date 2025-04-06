<template>
  <div class="profile-page">
    <h1 class="text-3xl font-bold mb-6">Личный кабинет</h1>
    <div v-if="user" class="bg-white shadow-md rounded-lg p-4 mb-6">
      <p><strong>Имя:</strong> {{ user.name }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
      <p><strong>Роль:</strong> {{ user.role_name }}</p>
      <button
        @click="logout"
        class="mt-4 px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500"
      >
        Выйти
      </button>
    </div>
    
    <div v-if="user">
      <h2 class="text-2xl font-bold mb-4">Мои вопросы</h2>
      <ul class="space-y-4">
        <li v-for="question in userQuestions" :key="question.id" class="bg-white shadow-md rounded-lg p-4">
          <router-link :to="`/question/${question.id}`" class="text-blue-600 hover:text-blue-800">
            {{ question.title }}
          </router-link>
          <div class="flex items-center mt-2 text-sm text-gray-500">
            <span>{{ formatDate(question.creation_time) }}</span>
          </div>
        </li>
      </ul>
      <p v-if="!userQuestions.length" class="text-gray-600">У вас нет вопросов.</p>
    </div>
    <p v-else>Загрузка...</p>
  </div>
</template>

<script>
import { ref, computed, watch, onMounted } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { fetchQuestionsByUser } from '@/services/forumApi';

export default {
  setup() {
    const store = useStore();
    const router = useRouter();
    const user = computed(() => store.getters.user);
    const userQuestions = ref([]);

    const loadUserQuestions = async () => {
      try {
        userQuestions.value = await fetchQuestionsByUser();
      } catch (error) {
        console.error('Ошибка при загрузке вопросов:', error);
        userQuestions.value = [];
      }
    };

    onMounted(() => {
      if (user.value) {
        loadUserQuestions();
      }
    });

    watch(
      () => user.value,
      (newUser) => {
        if (newUser) {
          loadUserQuestions();
        }
      }
    );

    const logout = async () => {
      try {
        await store.dispatch('logout');
        router.push('/login');
      } catch (error) {
        console.error('Ошибка при выходе:', error);
        alert('Ошибка при выходе. Попробуйте снова.');
      }
    };

    const formatDate = (date) => {
      return new Date(date).toLocaleDateString();
    };

    return { user, userQuestions, logout, formatDate };
  },
};
</script>