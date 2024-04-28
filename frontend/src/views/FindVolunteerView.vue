<template>
  <div class="bg-section-secondary w-full h-screen">
    <div class="flex justify-center h-screen">
      <Filters />
      <FindVolunteerFeed class="overflow-auto pb-10" />
    </div>
  </div>
</template>

<script setup>
import FindVolunteerFeed from '@/components/feed/FindVolunteerFeed.vue';
import Filters from '@/components/feed/filters/Filters.vue';
</script>
