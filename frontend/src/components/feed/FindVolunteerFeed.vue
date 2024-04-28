<template>
  <section class="flex flex-col justify-start mt-20 w-1/2">
    <SearchBar class="sticky top-0" />
    <div class="flex flex-col">
      <FeedCard v-for="(volunteer, index) in store.volunteers" :key="index" :data="volunteer" />
    </div>
  </section>
</template>

<script setup>
import { onMounted } from 'vue';
import { useFindFeedStore } from '@/stores/findFeed.js';
import FeedCard from '@/components/feed/card/FeedCard.vue';
import SearchBar from '@/components/feed/SearchBar.vue';

const store = useFindFeedStore();

onMounted(async () => {
  await store.fetchVolunteerData();
});
</script>

<style lang="scss" scoped></style>
