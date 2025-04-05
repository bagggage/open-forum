import { ref, onMounted } from 'vue';
import { loginUser as loginApi, logoutUser } from '@/services/authApi';

export const useAuth = () => {
  const isAuthenticated = ref(false);
  const user = ref(null);

  const login = async (email, password) => {
    try {
      const userData = await loginApi(email, password);
      user.value = { email, name: userData.name };
      isAuthenticated.value = true;
    } catch (error) {
      isAuthenticated.value = false;
      user.value = null;
      throw error;
    }
  };

  const logout = async () => {
    try {
      await logoutUser();
      isAuthenticated.value = false;
      user.value = null;
    } catch (error) {
      console.error('Ошибка при выходе:', error);
      throw error;
    }
  };

  const checkAuth = () => {
    isAuthenticated.value = !!user.value;
  };

  onMounted(() => {
    checkAuth();
  });

  return { isAuthenticated, user, login, logout };
};