<template>
  <section class="flex flex-col justify-start mt-20">
    <SearchBar class="sticky top-0" />
    <FeedCard v-for="(volunteer, index) in paginatedVolunteers" :key="index" :data="volunteer" />
    <!-- <div
      v-if="store.volunteers.length > itemsPerPage"
      class="flex justify-center gap-2 items-center mt-2"
    >
      <AppButton
        text="Prev"
        @click="currentPage--"
        :disabled="currentPage <= 0"
        class="bg-primary hover:bg-primary-dark text-white py-2 px-4"
      />

      <div class="font-semibold">Page: {{ currentPage + 1 }} of {{ pageCount }}</div>
      <AppButton
        text="Next"
        @click="currentPage++"
        :disabled="currentPage >= pageCount - 1"
        class="bg-primary hover:bg-primary-dark text-white py-2 px-4"
      />
    </div> -->
  </section>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import { useFindFeedStore } from '@/stores/findFeed.js';
import FeedCard from '@/components/feed/card/FeedCard.vue';
import SearchBar from '@/components/feed/SearchBar.vue';

const store = useFindFeedStore();
const itemsPerPage = 4;
const currentPage = ref(0);

const paginatedVolunteers = computed(() => {
  const start = currentPage.value * itemsPerPage;
  const end = start + itemsPerPage;
  return store.volunteers.slice(start, end);
});

onMounted(() => {
  store.fetchVolunteerData();
});
</script>

<style lang="scss" scoped></style>
