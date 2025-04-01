<template>
  <ul class="space-y-4">
    <li v-for="answer in answers" :key="answer.id" class="bg-gray-50 p-4 rounded-lg">
      <p class="text-gray-800">{{ answer.content }}</p>
      <div class="flex items-center mt-2 text-sm text-gray-500">
        <span>{{ answer.author }}</span>
        <span class="mx-2">•</span>
        <span>{{ formatDate(answer.createdAt) }}</span>
      </div>
    </li>
  </ul>
</template>

<script>
import { ref } from 'vue';

export default {
  props: {
    answers: {
      type: Array,
      default: () => [],
    },
  },
  setup() {
    const formatDate = (date) => {
      return new Date(date).toLocaleDateString();
    };

    return { formatDate };
  },
};
</script>