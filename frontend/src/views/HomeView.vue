<template>
  <div class="home">
    <h1>Добро пожаловать на форум</h1>

    <section class="mb-4">
      <label for="search-input" class="block text-sm font-medium text-gray-700">Поиск:</label>
      <input
        id="search-input"
        v-model="searchQuery"
        @input="filterQuestions"
        placeholder="Введите ключевое слово..."
        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
      />
    </section>

    <section class="mb-8">
      <label for="category-select" class="block text-sm font-medium text-gray-700">Выберите категорию:</label>
      <select
        id="category-select"
        v-model="selectedCategory"
        @change="resetPagination"
        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
      >
        <option value="">Все категории</option>
        <option v-for="category in categories" :key="category.id" :value="category.name">
          {{ category.name }}
        </option>
      </select>
    </section>

    <section>
      <h2>Последние вопросы</h2>
      <QuestionList
        :categoryName="selectedCategory"
        :searchQuery="searchQuery"
        :currentPage="currentPage"
        @update-page="updatePage"
      />
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
    const searchQuery = ref('');
    const currentPage = ref(0);

    onMounted(async () => {
      categories.value = await fetchCategories();
    });

    const resetPagination = () => {
      currentPage.value = 0;
    };

    const updatePage = (newPage) => {
      currentPage.value = newPage;
    };

    return { categories, selectedCategory, searchQuery, currentPage, resetPagination, updatePage };
  },
};
</script>
