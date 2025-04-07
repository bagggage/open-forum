<template>
  <ul class="space-y-4 mb-4">
    <li v-for="answer in answers" :key="answer.id">
      <AnswerItem :answer="answer" />
    </li>
  </ul>
</template>

<script>
import AnswerItem from './AnswerItem.vue'

export default {
  name: 'AnswerList',
  props: {
    answers: {
      type: Array,
      default: () => [],
    },
  },
  components: { AnswerItem },
  setup(props) {
    console.log(props.answers)
  }
};
</script>