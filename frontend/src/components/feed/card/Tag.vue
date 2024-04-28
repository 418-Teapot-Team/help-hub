<template>
  <section class="inline-block mx-1 bg-primary rounded-xl shadow-md max-w-sm">
    <div class="mx-5 text-white">
      <p>{{ text }}</p>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  text: {
    type: String,
    require: true,
  },
});

const text = ref(props.text);
</script>
