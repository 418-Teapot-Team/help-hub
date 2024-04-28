<template>
  <div class="bg-section-secondary w-full h-screenr flex justify-center">
    <div class="flex justify-center h-screen gap-x-4 container">
      <RequestList :data="requestsData" lass="overflow-auto pb-10" :isMy="true" />
    </div>
  </div>
</template>
<script setup>
import RequestList from '@/components/helpRequests/RequestList.vue';
import { useRequestsStore } from '@/stores/requests';
import { ref } from 'vue';
import { onBeforeMount } from 'vue';

const requestsStore = useRequestsStore();

const requestsData = ref([]);

onBeforeMount(() => {
  requestsStore.getMyRequests().then((res) => {
    requestsData.value = res;
  });
});
</script>
