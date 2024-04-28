<template>
  <section class="m-6 bg-white shadow-md max-w-6xl">
    <div class="flex gap-6 p-5">
      <div class="md:flex-shrink-0 self-start">
        <img class="object-contain w-16" :src="volunteer.image" />
      </div>
      <div class="text-start text-wrap">
        <p class="font-semibold text-3xl">{{ volunteer.name }}</p>
        <p>Зіроньки</p>
        <p class="opacity-75 font-semibold">{{ volunteer.location }}</p>
        <div class="mb-3 mt-2">
          <Tag v-for="(tag, index) in volunteer.tags" :key="index" :text="tag" />
        </div>

        <p class="opacity-75 font-semibold">{{ volunteer.description }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import Tag from '@/components/feed/feed/card/Tag.vue';

const props = defineProps({
  data: {
    type: Object,
    require: true,
  },
});

const volunteer = ref(props.data);
</script>

<style lang="scss" scoped></style>
