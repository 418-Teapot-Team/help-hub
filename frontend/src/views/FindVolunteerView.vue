<template>
  <div class="bg-section-secondary w-full">
    <div class="flex justify-center h-fit">
      <FindVolunteerFeed class="pb-10" :data="data" />
    </div>
  </div>
</template>

<script setup>
import FindVolunteerFeed from '@/components/feed/FindVolunteerFeed.vue';
import { useRequestsStore } from '@/stores/requests';
import { onMounted, ref } from 'vue';

const requestsStore = useRequestsStore();

const data = ref([]);

onMounted(() => {
  requestsStore.getVolunteers().then((res) => {
    data.value = res?.volunteers;
  });
});
</script>
