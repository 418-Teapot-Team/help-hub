<template>
  <section>
    <div class="hidden sm:block w-[250px] h-[700px] bg-white mt-20 px-8 py-6">
      <span class="text-4xl font-semibold">Фільтри</span>
      <FiltersVariants :title="'Міста'" :filters="filters.cities" />
      <FiltersVariants :title="'Спеціалізація'" :filters="filters.categories" />
      <div class="w-full h-[110px] flex flex-col justify-around items-center mt-4">
        <AppButton @on-click="applyFilters" text="Застосувати" isBold class="w-full py-1.5" />
        <AppButton
          text="Скинути"
          isBold
          buttonStyle="outline"
          class="w-full py-[6px]"
          @on-click="clearAllFilters"
        />
      </div>
    </div>
    <div class="fixed z-10 sm:hidden w-screen h-screen -mt-[80px]">
      <AppButton
        :text="isFilterOpen ? 'Hide filters' : 'Show filters'"
        class="sm:hidden fixed w-full bottom-0 bg-blue-300 px-8 py-6"
        @click="toggleFilter"
      />
      <div v-if="isFilterOpen" class="w-full h-full bg-white px-8 py-6">
        <span class="text-4xl font-semibold">Фільтри</span>
        <FiltersVariants :title="'Міста'" :filters="filters.cities" />
        <FiltersVariants :title="'Спеціалізація'" :filters="filters.categories" />
        <div class="w-full h-[110px] flex flex-col justify-around items-center mt-12">
          <AppButton text="Застосувати" isBold class="w-full py-1.5 fixed bottom-[75px]" />
          <AppButton
            text="Скинути"
            isBold
            buttonStyle="outline"
            class="w-full py-[6px]"
            @on-click="clearAllFilters"
          />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import { useFiltersStore } from '@/stores/filters.js';
import FiltersVariants from '@/components/feed/filters/FiltersVariants.vue';
import AppButton from '@/components/atoms/buttons/AppButton.vue';

defineProps(['filters']);

const emit = defineEmits(['applyFilters']);

const filtersStore = useFiltersStore();

const clearFilterButton = ref(false);

function clearAllFilters() {
  filtersStore.clearAllFilters();
  applyFilters();
  clearFilterButton.value = false;
}

function applyFilters() {
  clearFilterButton.value = true;
  emit('applyFilters');
}

const isFilterOpen = ref(false);
const toggleFilter = () => {
  isFilterOpen.value = !isFilterOpen.value;
};
</script>
