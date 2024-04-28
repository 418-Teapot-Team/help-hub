<template>
  <div class="bg-section-secondary w-screen h-screen">
    <Filters />
    <div class="flex justify-center h-screen">
      <FindVolunteerFeed />
    </div>
  </div>
</template>

<script setup>
import FindVolunteerFeed from '@/components/feed/FindVolunteerFeed.vue';
import Filters from '@/components/feed/filters/Filters.vue';
</script>
