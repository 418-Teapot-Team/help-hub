<template>
  <div class="bg-section-secondary w-screen h-screen">
    <FeedCard />
    <Filters />
  </div>
</template>

<script setup>
import FeedCard from '@/components/feed/card/FeedCard.vue';
import Filters from '@/components/feed/filters/Filters.vue';
</script>
