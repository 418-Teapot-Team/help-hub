<template>
  <div class="mx-9 bg-white rounded-xl shadow-md max-w-xs m-3 w-52">
    <div class="md:grid grid-cols-1 place-items-center">
      <div class="md:flex-shrink-0">
        <img class="object-cover h-20 w-20" src="/images/hand-up.png" alt="An image" />
      </div>
      <div class="p-8 text-center">
        <div class="uppercase tracking-wide text-2xl text-primary font-bold">{{ stat }}</div>
        <p class="mt-2 text-gray-500 text-md font-bold">{{ label }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps } from 'vue';

const props = defineProps({
  stat: {
    type: Number,
    required: true,
  },
  label: {
    type: String,
    required: true,
  },
});

const stat = ref(props.stat);
const label = ref(props.label);
</script>

<style lang="scss" scoped></style>
