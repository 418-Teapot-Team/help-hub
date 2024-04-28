<template>
  <div class="pt-6">
    <div class="mb-2">
      <button class="w-full flex" @click="toggleFilter">
        <label class="text-xl font-semibold">{{ title }}</label>
        <span class="ml-1 text-gray-500" v-if="selectedFiltersLength > 0">
          ({{ selectedFiltersLength }})
        </span>
        <ArrowIcon class="duration-200" :class="{ '-rotate-90 ': !isOpen }" />
      </button>
    </div>
    <div v-if="isOpen">
      <div v-for="(item, idx) in filters" :key="idx" class="mb-2 pl-2 flex">
        <AppCheckboxInput :id="idx + 1" v-model="item.isSelected" class="mr-2" />
        <label :for="idx">{{ item.name }}</label>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, computed, ref } from 'vue';
import AppCheckboxInput from '@/components/atoms/inputs/AppCheckboxInput.vue';
import ArrowIcon from '@/components/icons/ArrowIcon.vue';

const { title, filters } = defineProps(['title', 'filters']);

const selectedFiltersLength = computed(() => {
  const selectedFilters = filters.filter((item) => item.isSelected);
  return selectedFilters.length;
});

const isOpen = ref(true);
const toggleFilter = () => {
  isOpen.value = !isOpen.value;
};
</script>
