<template>
  <div class="profile-page">
    <h1 class="prime-color">Личный кабинет</h1>
    <div v-if="user" class="profile-panel">
      <p><strong>Имя:</strong> {{ user.name }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
      <p><strong>Роль:</strong> {{ user.role_name }}</p>
      <button @click="logout" class="btn-red btn">Выйти</button>
    </div>
    
    <div v-if="user">
      <h2>Мои вопросы</h2>
      <QuestionList :questions="userQuestions"/>
    </div>
    <p v-else>Загрузка...</p>
  </div>
</template>

<script>
import { ref, computed, watch, onMounted } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { fetchQuestionsByUser } from '@/services/forumApi';
import QuestionList from '@/components/QuestionList.vue';

export default {
  components: { QuestionList },
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