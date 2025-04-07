<template>
  <div class="login-page">
    <h1>Вход</h1>
    <form @submit.prevent="login" class="space-y-4">
      <div>
        <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div>
        <label for="password" class="block text-sm font-medium text-gray-700">Пароль</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit" class="btn w-full">Войти</button>
      <p class="text-center text-gray-600">
        Нет аккаунта?
        <router-link to="/register" class="text-blue-600 hover:text-blue-800">
          Зарегистрироваться
        </router-link>
      </p>
    </form>
  </div>
</template>
<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';

export default {
  setup() {
    const email = ref('');
    const password = ref('');
    const router = useRouter();
    const store = useStore();

    const login = async () => {
      try {
        await store.dispatch('login', { email: email.value, password: password.value });
        router.push('/profile');
      } catch (error) {
        console.error('Ошибка при входе:', error);
        alert('Неверный email или пароль.');
      }
    };

    return { email, password, login };
  },
};
</script>