<template>
  <div class="mx-9 pt-5 bg-white shadow-md m-3 w-28 h-56 md:w-48">
    <div class="grid grid-cols-1 place-items-center">
      <div class="md:flex-shrink-0 pt-5">
        <img class="object-contain h-16" :src="image" />
      </div>
      <div class="p-8 text-center text-wrap">
        <div class="uppercase tracking-wide text-2xl text-primary font-bold">{{ stat }}</div>
        <p class="mt-2 text-gray-500 text-md font-bold">{{ label }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  stat: {
    type: String,
    required: true,
  },
  label: {
    type: String,
    required: true,
  },
  image: {
    type: String,
    required: false,
  },
});

const stat = ref(props.stat);
const label = ref(props.label);
const image = ref(props.image);
</script>

<style lang="scss" scoped></style>
