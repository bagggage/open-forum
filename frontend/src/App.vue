<template>
  <div class="app-container">
    <!-- Навигация -->
    <nav class="bg-gray-800 text-white py-4 px-6">
      <div class="container mx-auto flex justify-between items-center">
        <h1 class="text-2xl font-bold">Форум</h1>
        <div class="space-x-4">
          <router-link to="/" class="text-white hover:text-gray-300">Главная</router-link>
          <router-link to="/categories" class="text-white hover:text-gray-300">Категории</router-link>
          <router-link v-if="!isAuthenticated" to="/login" class="text-white hover:text-gray-300">Вход</router-link>
          <router-link v-else to="/profile" class="text-white hover:text-gray-300">Личный кабинет</router-link>
        </div>
      </div>
    </nav>

    <!-- Основное содержимое -->
    <main class="container mx-auto p-6">
      <router-view />
    </main>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'App',
  setup() {
    // Пример состояния аутентификации (замените на реальную логику)
    const isAuthenticated = ref(false);

    return { isAuthenticated };
  },
};
</script>

<style>
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>