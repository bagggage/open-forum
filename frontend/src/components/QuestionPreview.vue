<template>
    <div class="question-preview">
        <router-link :to="`/question/${question.id}`">
            <h3>{{ question.title }}</h3>
        </router-link>
        <div class="flex items-center mt-2">
          <span>{{ question.user_name }}</span>
          <span class="mx-2">•</span>
          <span>{{ formatDate(question.creation_time) }}</span>
        </div>
    </div>
</template>

<script>
export default {
    name: `QuestionPreview`,
    props: ['question'],
    setup() {
        const formatDate = (date) => {
          return new Date(date).toLocaleDateString();
        };

        return { formatDate }
    }
}
</script>