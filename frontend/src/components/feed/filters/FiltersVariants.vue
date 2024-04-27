<template>
  <div class="pt-6">
    <div class="mb-2">
      <label class="text-xl font-semibold">{{ title }}</label>
      <span class="ml-1 text-gray-500" v-if="selectedFiltersLength > 0">
        ({{ selectedFiltersLength }})
      </span>
    </div>
    <div v-for="(item, idx) in filters" :key="idx" class="mb-2 pl-2 flex">
      <AppCheckboxInput :id="idx + 1" v-model="item.isSelected" class="mr-2" />
      <label :for="idx">{{ item.name }}</label>
    </div>
  </div>
</template>

<script setup>
import { defineProps, computed } from 'vue';
import AppCheckboxInput from '@/components/atoms/inputs/AppCheckboxInput.vue';

const { title, filters } = defineProps(['title', 'filters']);

const selectedFiltersLength = computed(() => {
  const selectedFilters = filters.filter((item) => item.isSelected);
  return selectedFilters.length;
});
</script>
