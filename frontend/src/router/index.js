import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import CategoryListView from '@/views/CategoryView.vue';
import LoginView from '@/views/LoginView.vue';
import RegisterView from '@/views/RegisterView.vue';
import ProfileView from '@/views/ProfileView.vue';
import QuestionDetailView from '@/views/QuestionDetailView.vue';
import CreateQuestionView from '@/views/CreateQuestionView.vue';
import store from '@/store';

const routes = [
  { path: '/', component: HomeView, name: 'Home' },
  { path: '/categories', component: CategoryListView, name: 'Categories' },
  { path: '/login', component: LoginView, name: 'Login', meta: { requiresUnauth: true } },
  { path: '/register', component: RegisterView, name: 'Register', meta: { requiresUnauth: true } },
  { path: '/profile', component: ProfileView, name: 'Profile', meta: { requiresAuth: true } },
  { path: '/question/:id', component: QuestionDetailView, name: 'QuestionDetail' },
  { path: '/ask', component: CreateQuestionView, name: 'CreateQuestion', meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach(async (to, from, next) => {
  if (to.meta.requiresAuth && !store.getters.isAuthenticated) {
    next('/login');
  } else if (to.meta.requiresUnauth && store.getters.isAuthenticated) {
    next('/');
  } else {
    next();
  }
});

export default router;