<template>
  <section class="flex flex-col justify-center my-9">
    <div class="flex justify-center mb-4">
      <!-- TODO: add debounce for search-->
      <div class="border-2 border-primary rounded mr-2 w-3/5">
        <input
          v-model="searchTerm"
          type="text"
          placeholder="Search volunteers..."
          class="m-2 rounded"
        />
      </div>
      <!-- TODO: send the search request to server -->
      <button
        @click="search"
        class="bg-primary hover:bg-primary-dark text-white font-bold py-2 px-4 rounded"
      >
        Search
      </button>
    </div>
    <FeedCard v-for="(volunteer, index) in paginatedVolunteers" :key="index" :data="volunteer" />
    <div
      v-if="store.volunteers.length > itemsPerPage"
      class="flex justify-center gap-2 items-center"
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
import FeedCard from '@/components/feed/card/FeedCard.vue';
import { onMounted, ref, computed } from 'vue';
import { useFindFeedStore } from '@/stores/findFeed.js';

const store = useFindFeedStore();
const itemsPerPage = 3;
const currentPage = ref(0);
const searchTerm = ref('');

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
