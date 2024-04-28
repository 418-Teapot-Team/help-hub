<template>
  <div class="bg-section-secondary w-full min-h-screen flex justify-center">
    <div class="flex justify-center gap-x-4 container pb-10">
      <Filters :filters="filtersData" @applyFilters="applyFilters" />
      <RequestList :data="requestsData" lass="" />
    </div>
  </div>
</template>
<script setup>
import Filters from '@/components/feed/filters/Filters.vue';
import RequestList from '@/components/helpRequests/RequestList.vue';
import { useRequestsStore } from '@/stores/requests';
import { onMounted, ref } from 'vue';
import { onBeforeMount } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useFiltersStore } from '@/stores/filters';

const filtersStore = useFiltersStore();
const requestsStore = useRequestsStore();
const route = useRoute();
const router = useRouter();

const filtersData = ref({});
const requestsData = ref([]);

onBeforeMount(() => {
  requestsStore.getRequests(parseQuery(route.query)).then((res) => {
    requestsData.value = res.requests;
    filtersData.value = res.filters;
  });
});

onMounted(() => {
  filtersStore.parseFromQuery(route.query);
});

function parseQuery(query) {
  let parsedQuery = {};
  if (query) {
    Object.keys(query).map((key) => {
      parsedQuery[key] = JSON.parse(query[key]);
    });
  }
  return parsedQuery;
}

function applyFilters() {
  router.push(filtersStore.getQuerystring()).then(() => {
    requestsStore.getRequests(parseQuery(route.query)).then((res) => {
      requestsData.value = res.requests;
      filtersData.value = res.filters;
    });
  });
}
</script>
