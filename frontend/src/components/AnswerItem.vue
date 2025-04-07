<template>
  <div class="answer-item">
    <p>{{ answer.text }}</p>
    <div class="flex items-center mt-2 text-sm text-gray-500">
      <span>{{ answer.user_name }}</span>
      <span class="mx-2">•</span>
      <span>{{ formatDate(answer.creation_time) }}</span>
    </div>
  </div>
</template>

<script>
export default {
    name: `AnswerItem`,
    props: ['answer'],
    setup() {
      const formatDate = (date) => {
        return new Date(date).toLocaleDateString();
      };

      return { formatDate };
    },
}
</script>
