import { createStore } from 'vuex';
import { logoutUser } from '@/services/authApi';

export default createStore({
  state: {
    user: null,
    isAuthenticated: false,
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user;
      state.isAuthenticated = !!user;
    },
    LOGOUT(state) {
      state.user = null;
      state.isAuthenticated = false;
    },
  },
  actions: {
    setUser({ commit }, user) {
      commit('SET_USER', user);
    },
    async logout({ commit }) {
      try {
        await logoutUser();
        commit('LOGOUT');
      } catch (error) {
        console.error('Ошибка при выходе:', error);
        throw error;
      }
    },
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
    user: (state) => state.user,
  },
});