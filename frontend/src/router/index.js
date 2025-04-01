import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import CategoryListView from '@/views/CategoryView.vue';
import LoginView from '@/views/LoginView.vue';
import ProfileView from '@/views/ProfileView.vue';

const routes = [
  { path: '/', component: HomeView, name: 'Home' },
  { path: '/categories', component: CategoryListView, name: 'Categories' },
  { path: '/login', component: LoginView, name: 'Login' },
  { path: '/profile', component: ProfileView, name: 'Profile' },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;  