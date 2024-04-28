import { defineStore } from 'pinia';
import { ref } from 'vue';
import { httpClient } from '@/utils/HttpClient';

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
  async function getFilters() {
    const { data } = await httpClient.get('');
    this.cities = data.cities.result;
    this.spec = data.spec.result;
  }

  async function applyFilters() {
    const selectedCities = this.cities.filter((city) => city.isSelected).map((city) => city.name);
    const selectedSpec = this.spec.filter((spec) => spec.isSelected).map((spec) => spec.name);

    const filtersData = {
      cities: selectedCities,
      spec: selectedSpec,
    };

    await httpClient.post('', filtersData);
  }

  return {
    cities,
    spec,
    resetFilters,
    getFilters,
    applyFilters,
  };
});
