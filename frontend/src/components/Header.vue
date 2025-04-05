<template>
  <nav class="bg-gray-800 text-white py-4 px-6">
    <div class="container mx-auto flex justify-between items-center">
      <h1 class="text-2xl font-bold">Форум</h1>
      <div class="space-x-4">
        <router-link to="/" class="text-white hover:text-gray-300">Главная</router-link>
        <router-link to="/categories" class="text-white hover:text-gray-300">Категории</router-link>
        <router-link v-if="isAuthenticated" to="/profile" class="text-white hover:text-gray-300">Личный кабинет</router-link>
        <router-link v-else to="/login" class="text-white hover:text-gray-300">Вход</router-link>
      </div>
    </div>
  </nav>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
  name: 'Header',
  setup() {
    const store = useStore();
    const isAuthenticated = computed(() => store.getters.isAuthenticated);

    return { isAuthenticated };
  },
};
</script>