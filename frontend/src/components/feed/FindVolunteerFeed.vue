<template>
  <section class="flex flex-col justify-start mt-20 w-1/2">
    <div class="flex flex-col">
      <FeedCard v-for="(volunteer, index) in data" :key="index" :data="volunteer" />
    </div>
  </section>
</template>

<script setup>
import FeedCard from '@/components/feed/card/FeedCard.vue';
defineProps(['data']);
</script>

<style lang="scss" scoped></style>
