import { createStore } from 'vuex';
import { loginUser, logoutUser } from '@/services/authApi';
import { fetchCurrentUser } from '@/services/forumApi';

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
    async fetchUser({ commit }) {
      try {
        const user = await fetchCurrentUser();
        commit('SET_USER', user);
      } catch (error) {
        commit('LOGOUT');
      }
    },
    async login({ dispatch }, { email, password }) {
      await loginUser(email, password);
      await dispatch('fetchUser');
    },
    async logout({ commit }) {
      await logoutUser();
      commit('LOGOUT');
    },
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
    user: (state) => state.user,
  },
});