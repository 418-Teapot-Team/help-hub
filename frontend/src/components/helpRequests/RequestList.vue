<template>
  <div
    class="flex flex-col justify-start items-center w-full gap-y-4 max-h-[calc(100vh-115px)] overflow-auto"
  >
    <RequestCard />
    <RequestCard :is-my-request="true" />
    <RequestCard :is-my-apply="true" status="pending" />
    <RequestCard :is-my-apply="true" status="denied" />
    <RequestCard :is-my-apply="true" status="accepted" />
  </div>
</template>
<script setup>
import RequestCard from './RequestCard.vue';
</script>
