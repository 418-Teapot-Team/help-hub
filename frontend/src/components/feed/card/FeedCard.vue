<template>
  <section class="m-6 bg-white shadow-md max-w-6xl">
    <div class="flex gap-6 p-5">
      <div class="md:flex-shrink-0 self-start">
        <img class="object-contain w-16" :src="volunteer.image" />
      </div>
      <div class="text-start text-wrap">
        <p class="font-semibold text-3xl">{{ volunteer.name }}</p>
        <p class="text-light-text font-semibold">{{ volunteer.location }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  data: {
    type: Object,
    require: true,
  },
});

const volunteer = ref(props.data);
</script>

<style lang="scss" scoped></style>
