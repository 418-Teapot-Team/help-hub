<template>
  <div class="bg-section-secondary w-screen h-screen flex justify-center">
    <div class="container h-full flex flex-row justify-center gap-10 pt-16">
      <Filters class="-mt-20" />
      <div class="flex justify-center h-screen w-full">
        <RequestList />
      </div>
    </div>
  </div>
</template>
<script setup>
import Filters from '@/components/feed/filters/Filters.vue';
import RequestList from '@/components/helpRequests/RequestList.vue';
</script>
