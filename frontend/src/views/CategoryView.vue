<template>
  <div class="category-list-page">
    <h1 class="text-3xl font-bold mb-6">Категории</h1>

    <section>
      <CategoryList />
    </section>
  </div>
</template>

<script>
import CategoryList from '@/components/CategoryList.vue';

export default {
  name: 'CategoryListView',
  components: { CategoryList },
};
</script>

<style scoped>
.category-list-page {
  padding: 20px;
}
</style>