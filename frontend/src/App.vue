<template>
  <div class="app-container">
    <Header />
    <main class="main-container">
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

<style lang="scss">
@use './assets/style.scss';
</style>