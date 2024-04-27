<template>
  <section class="w-[250px] h-[700px] bg-white m-16 ml-28 absolute px-8 py-6">
    <span class="text-4xl font-semibold">Фільтри</span>
    <FiltersVariants :title="'Міста'" :filters="cities" />
    <FiltersVariants :title="'Спеціалізація'" :filters="spec" />
    <div class="w-full h-[110px] flex flex-col justify-around items-center mt-4">
      <AppButton text="Застосувати" isBold class="w-full py-1.5" />
      <AppButton text="Скинути" isBold buttonStyle="outline" class="w-full py-[6px]" />
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import FiltersVariants from '@/components/feed/filters/FiltersVariants.vue';
import AppButton from '../../atoms/buttons/AppButton.vue';
const cities = ref([
  { name: 'Львів', isSelected: false },
  { name: 'Тернопіль', isSelected: false },
  { name: 'Хмельницький', isSelected: false },
  { name: 'Вінниця', isSelected: false },
  { name: 'Київ', isSelected: false },
  { name: 'Дніпро', isSelected: false },
]);

const spec = ref([
  { name: 'Дрони', isSelected: false },
  { name: 'Автомобілі', isSelected: false },
  { name: 'Електроніка', isSelected: false },
  { name: 'Лопата', isSelected: false },
  { name: 'Література', isSelected: false },
  { name: 'Гроші', isSelected: false },
]);
</script>
