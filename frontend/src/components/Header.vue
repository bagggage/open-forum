<template>
  <nav class="header">
    <div class="container mx-auto flex justify-between items-center">
      <div class="logo">
        <h1>Open Forum</h1>
      </div>
      <div class="space-x-2">
        <router-link to="/" class="link-btn">Главная</router-link>
        <router-link to="/categories" class="link-btn">Категории</router-link>
        <router-link v-if="!isAuthenticated" to="/login" class="link-btn">Вход</router-link>
        <router-link v-else to="/profile" class="link-btn">Личный кабинет</router-link>
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

    // Получаем состояние аутентификации через геттер
    const isAuthenticated = computed(() => store.getters.isAuthenticated);

    // Действие для выхода
    const logout = () => {
      store.dispatch('logout');
      // Можно добавить перенаправление:
      // router.push('/login');
    };

    return { isAuthenticated, logout };
  },
};
</script>