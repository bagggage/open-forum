<template>
  <ul class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
    <li v-for="category in categories" :key="category.id" class="bg-white shadow-md rounded-lg p-4">
      <span class="text-xl font-semibold text-blue-600">{{ category.name }}</span>
    </li>
  </ul>
</template>

<script>
import { ref, onMounted } from 'vue';
import { fetchCategories } from '@/services/forumApi';

export default {
  setup() {
    const categories = ref([]);

    onMounted(async () => {
      categories.value = await fetchCategories();
    });

    return { categories };
  },
};
</script>