<template>
  <nav class="bg-gray-800 text-white py-4 px-6">
    <div class="container mx-auto flex justify-between items-center">
      <h1 class="text-2xl font-bold">Форум</h1>
      <div class="space-x-4">
        <router-link to="/" class="text-white hover:text-gray-300">Главная</router-link>
        <router-link to="/categories" class="text-white hover:text-gray-300">Категории</router-link>
        <router-link
          v-if="isAuthenticated"
          to="/ask"
          class="text-white hover:text-gray-300"
        >
          Задать вопрос
        </router-link>
        <router-link v-if="!isAuthenticated" to="/login" class="text-white hover:text-gray-300">Вход</router-link>
        <router-link v-else to="/profile" class="text-white hover:text-gray-300">Личный кабинет</router-link>
      </div>
    </div>
  </nav>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
  name: 'AppHeader',
  setup() {
    const store = useStore();
    const isAuthenticated = computed(() => store.getters.isAuthenticated);

    return { isAuthenticated };
  },
};
</script>