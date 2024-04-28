<template>
  <div class="bg-section-secondary w-ful min-h-screen flex justify-center">
    <div class="flex justify-center h-fit sm:container">
      <RequestList :data="appliesData" lass="pb-10" :isApp="true" />
    </div>
  </div>
</template>
<script setup>
import RequestList from '@/components/helpRequests/RequestList.vue';
import { useRequestsStore } from '@/stores/requests';
import { ref } from 'vue';
import { onBeforeMount } from 'vue';

const requestsStore = useRequestsStore();

const appliesData = ref([]);

onBeforeMount(() => {
  requestsStore.getMyApplies().then((res) => {
    appliesData.value = res;
  });
});
</script>
