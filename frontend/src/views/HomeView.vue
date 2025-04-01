<template>
  <div class="home">
    <h1 class="text-3xl font-bold mb-6">Добро пожаловать на форум</h1>

    <!-- Последние вопросы -->
    <section>
      <h2 class="text-2xl font-bold mb-4">Последние вопросы</h2>
      <QuestionList />
    </section>
  </div>
</template>

<script>
import QuestionList from '@/components/QuestionList.vue';

export default {
  name: 'HomeView',
  components: { QuestionList },
};
</script>

<style scoped>
.home {
  padding: 20px;
}
</style>