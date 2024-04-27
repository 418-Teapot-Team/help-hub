import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useFiltersStore = defineStore('filters', () => {
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

  function resetFilters() {
    cities.value = cities.value.map((city) => ({
      ...city,
      isSelected: false,
    }));
    spec.value = spec.value.map((specialization) => ({
      ...specialization,
      isSelected: false,
    }));
  }
  return {
    cities,
    spec,
    resetFilters,
  };
});
