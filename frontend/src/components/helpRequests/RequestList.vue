<template>
  <div class="flex flex-col justify-start mt-20 gap-y-4 w-full">
    <RequestCard v-for="item in data" :key="`req_${item.id}`" :data="item" :isMyRequest="isMy" />
  </div>
</template>
<script setup>
import RequestCard from './RequestCard.vue';
defineProps(['data', 'isMy']);
</script>
