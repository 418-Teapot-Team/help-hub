<template>
  <section class="flex flex-col justify-start mt-6">
    <SearchBar />
    <FeedCard v-for="(volunteer, index) in paginatedVolunteers" :key="index" :data="volunteer" />
    <div
      v-if="store.volunteers.length > itemsPerPage"
      class="flex justify-center gap-2 items-center mt-2"
    >
      <button
        @click="currentPage--"
        :disabled="currentPage <= 0"
        class="bg-primary hover:bg-primary-dark text-white font-bold py-2 px-4"
      >
        Prev
      </button>
      <div class="font-semibold">Page: {{ currentPage + 1 }} of {{ pageCount }}</div>
      <button
        @click="currentPage++"
        :disabled="currentPage >= pageCount - 1"
        class="bg-primary hover:bg-primary-dark text-white font-bold py-2 px-4"
      >
        Next
      </button>
    </div>
  </section>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import { useFindFeedStore } from '@/stores/findFeed.js';
import FeedCard from '@/components/feed/feed/card/FeedCard.vue';
import SearchBar from '@/components/feed/feed/SearchBar.vue';

const store = useFindFeedStore();
const itemsPerPage = 3;
const currentPage = ref(0);

const paginatedVolunteers = computed(() => {
  const start = currentPage.value * itemsPerPage;
  const end = start + itemsPerPage;
  return store.volunteers.slice(start, end);
});

const pageCount = computed(() => Math.ceil(store.volunteers.length / itemsPerPage));

onMounted(async () => {
  await store.fetchVolunteerData();
});
</script>

<style lang="scss" scoped></style>
