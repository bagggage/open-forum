<template>
  <div class="profile-page">
    <h1>Личный кабинет</h1>
    <div v-if="user" class="bg-white shadow-md rounded-lg p-4">
      <p><strong>Email:</strong> {{ user.email }}</p>
      <button
        @click="logout"
        class="mt-4 px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500"
      >
        Выйти
      </button>
    </div>
    <p v-else>Загрузка...</p>
  </div>
</template>
<script>
import { computed } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const store = useStore();
    const router = useRouter();
    const user = computed(() => store.getters.user);

    const logout = async () => {
      try {
        await store.dispatch('logout');
        router.push('/login');
      } catch (error) {
        console.error('Ошибка при выходе:', error);
        alert('Ошибка при выходе. Попробуйте снова.');
      }
    };

    return { user, logout };
  },
};
</script>