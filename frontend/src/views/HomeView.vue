<template>
  <div class="home">
    <h1 class="text-3xl font-bold mb-6">Добро пожаловать на форум</h1>

    <!-- Выбор категории -->
    <section class="mb-8">
      <label for="category-select" class="block text-sm font-medium text-gray-700">Выберите категорию:</label>
      <select
        id="category-select"
        v-model="selectedCategory"
        @change="filterQuestions"
        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
      >
        <option value="">Все категории</option>
        <option v-for="category in categories" :key="category.id" :value="category.name">
          {{ category.name }}
        </option>
      </select>
    </section>

    <!-- Вопросы -->
    <section>
      <h2 class="text-2xl font-bold mb-4">Последние вопросы</h2>
      <QuestionList :categoryName="selectedCategory" />
    </section>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { fetchCategories } from '@/services/forumApi';
import QuestionList from '@/components/QuestionList.vue';

export default {
  name: 'HomeView',
  components: { QuestionList },
  setup() {
    const categories = ref([]);
    const selectedCategory = ref('');

    onMounted(async () => {
      categories.value = await fetchCategories();
    });

    const filterQuestions = () => {
      // При выборе категории компонент QuestionList автоматически обновится
    };

    return { categories, selectedCategory, filterQuestions };
  },
};
</script>

<style scoped>
.home {
  padding: 20px;
}
</style>