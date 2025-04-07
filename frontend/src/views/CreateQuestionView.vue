<template>
  <div class="create-question-page">
    <h1 class="text-3xl font-bold mb-6">Создать вопрос</h1>
    <form @submit.prevent="submitQuestion" class="space-y-4">
      <div>
        <label for="title" class="block text-sm font-medium text-gray-700">Заголовок</label>
        <input type="text" id="title" v-model="title" required class="w-full" />
      </div>
      <div>
        <label for="text" class="block text-sm font-medium text-gray-700">Текст вопроса</label>
        <textarea id="text" v-model="text" required class="w-full" />
      </div>
      <div>
        <label for="category" class="block text-sm font-medium text-gray-700">Категория</label>
        <select id="category" v-model="category" required class="w-full">
          <option v-for="cat in categories" :key="cat.id" :value="cat.name">
            {{ cat.name }}
          </option>
        </select>
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700">Теги</label>
        <div class="flex items-center space-x-2 mb-2">
          <select v-model="selectedTag" class=" w-full">
            <option v-for="tag in availableTags" :key="tag.id" :value="tag.name">
              {{ tag.name }}
            </option>
          </select>
          <button
            type="button"
            @click="addTag"
            class="btn"
          >
            Добавить тег
          </button>
        </div>
        <div v-if="selectedTags.length" class="flex flex-wrap gap-2">
          <span
            v-for="tag in selectedTags"
            :key="tag"
            class="bg-blue-200 text-blue-800 px-3 py-1 rounded-full"
          >
            {{ tag }}
          </span>
        </div>
        <p v-else class="text-gray-500">Теги не выбраны</p>
      </div>
      <button
        type="submit"
        class="btn w-full"
      >
        Создать
      </button>
    </form>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { fetchCategories, fetchTags, createQuestion } from '@/services/forumApi';

export default {
  setup() {
    const router = useRouter();
    const title = ref('');
    const text = ref('');
    const category = ref('');
    const selectedTag = ref('');
    const selectedTags = ref([]);
    const categories = ref([]);
    const availableTags = ref([]);

    onMounted(async () => {
      categories.value = await fetchCategories();
      availableTags.value = await fetchTags();
    });

    const addTag = () => {
      if (selectedTag.value && !selectedTags.value.includes(selectedTag.value)) {
        selectedTags.value.push(selectedTag.value);
        selectedTag.value = '';
      }
    };

    const submitQuestion = async () => {
      try {
        await createQuestion({
          title: title.value,
          text: text.value,
          category_name: category.value,
          tag_names: selectedTags.value,
        });
        alert('Вопрос создан!');
        router.push('/');
      } catch (error) {
        console.error('Ошибка при создании вопроса:', error);
        alert('Ошибка при создании вопроса. Попробуйте снова.');
      }
    };

    return {
      title,
      text,
      category,
      selectedTag,
      selectedTags,
      categories,
      availableTags,
      addTag,
      submitQuestion,
    };
  },
};
</script>