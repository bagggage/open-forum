import { createStore } from 'vuex'

export default createStore({
  state() {
    return {
      isAuthenticated: false,
      user: null
    };
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
  },
  mutations: {
    login(state, userData) {
      state.isAuthenticated = true;
      state.user = userData;
    },
    logout(state) {
      state.isAuthenticated = false;
      state.user = null;
    },
  },
  actions: {
    login({ commit }, userData) {
      commit('login', userData);
    },
    logout({ commit }) {
      commit('logout');
    },
  },
  modules: {
  }
})
