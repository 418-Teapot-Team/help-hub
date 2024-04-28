<template>
  <section class="w-[250px] h-[700px] bg-white px-8 py-6">
    <span class="text-4xl font-semibold">Фільтри</span>
    <FiltersVariants :title="'Міста'" :filters="store.cities" />
    <FiltersVariants :title="'Спеціалізація'" :filters="store.spec" />
    <div class="w-full h-[110px] flex flex-col justify-around items-center mt-4">
      <AppButton text="Застосувати" isBold class="w-full py-1.5" />
      <AppButton
        text="Скинути"
        isBold
        buttonStyle="outline"
        class="w-full py-[6px]"
        @click="store.resetFilters"
      />
    </div>
  </section>
</template>

<script setup>
import { useFiltersStore } from '@/stores/filters.js';
import FiltersVariants from '@/components/feed/filters/FiltersVariants.vue';
import AppButton from '@/components/atoms/buttons/AppButton.vue';

const store = useFiltersStore();
</script>
