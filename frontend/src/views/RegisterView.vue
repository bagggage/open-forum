<template>
    <div class="register-page">
      <h1>Регистрация</h1>
      <form @submit.prevent="register" class="space-y-4">
        <div>
          <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <div>
          <label for="password" class="block text-sm font-medium text-gray-700">Пароль</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <div>
          <label for="name" class="block text-sm font-medium text-gray-700">Имя</label>
          <input type="text" id="name" v-model="name" required />
        </div>
        <button type="submit" class="btn w-full">Зарегистрироваться</button>
        <p class="text-center text-gray-600">
          Уже есть аккаунт?
          <router-link to="/login" class="text-blue-600 hover:text-blue-800">
            Войти
          </router-link>
        </p>
      </form>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import { registerUser } from '@/services/authApi';
  
  export default {
    setup() {
      const email = ref('');
      const password = ref('');
      const name = ref('');
      const router = useRouter();
  
      const register = async () => {
        try {
          await registerUser(email.value, password.value, name.value);
          alert('Регистрация успешна! Теперь войдите в аккаунт.');
          router.push('/login');
        } catch (error) {
          console.error('Ошибка при регистрации:', error);
          alert('Ошибка при регистрации. Попробуйте снова.');
        }
      };
  
      return { email, password, name, register };
    },
  };
  </script>