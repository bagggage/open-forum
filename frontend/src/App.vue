<template>
  <div class="app-container">
    <Header />
    <main class="container mx-auto p-6">
      <router-view />
    </main>
  </div>
</template>

<script>
import Header from './components/Header.vue';

export default {
  name: 'App',
  components: { Header },
};
</script>

<style>
@import './assets/style.scss';
</style>