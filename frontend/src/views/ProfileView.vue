<template>
  <div class="profile-page">
    <h1 class="text-3xl font-bold mb-6">Личный кабинет</h1>
    <p><strong>Email:</strong> user@example.com</p>
    <p><strong>Имя пользователя:</strong> JohnDoe</p>
    <button
      @click="logout"
      class="mt-4 px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500"
    >
      Выйти
    </button>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
  name: 'ProfileView',
  setup() {
    const router = useRouter();

    const logout = () => {
      // Здесь должна быть логика выхода (например, очистка токена)
      console.log('Пользователь вышел');
      router.push('/login');
    };

    return { logout };
  },
};
</script>

<style scoped>
.profile-page {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
}
</style>