<template>
  <header class="h-20 px-8 py-2 flex items-center justify-between shadow-md">
    <div class="flex items-center">
      <img src="/images/HandToHandLogo.webp" class="object-contain w-20" />
    </div>
    <ul class="hidden md:flex flex-1 justify-center gap-x-10">
      <li
        v-for="(item, idx) in headerLinks"
        :key="idx"
        class="text-dark-text text-lg hover:underline"
      >
        <router-link :to="item.url">
          {{ item.label }}
        </router-link>
      </li>
    </ul>
    <div>
      <div class="md:flex hidden justify-center items-center gap-x-6">
        <button class="px-3 py-2"><span class="font-semibold hover:underline">Вхід</span></button>
        <AppButton text="Реєстрація" isBold />
      </div>
      <BurgerIconVue @click="toggleDropdown" class="object-contain w-10 md:hidden" />
      <div v-if="isDropdownOpen" class="flex flex-col">
        <ul
          class="absolute z-10 w-full flex flex-col items-start top-20 right-0 bg-white shadow-md md:hidden"
        >
          <li
            v-for="(item, idx) in headerLinks"
            :key="idx"
            class="text-dark-text text-xl w-full h-full px-4 py-2 hover:bg-primary"
          >
            <router-link :to="item.url">
              {{ item.label }}
            </router-link>
          </li>
          <div class="p-4 flex justify-end w-full">
            <button class="px-3 py-2">
              <span class="font-semibold hover:underline">Вхід</span>
            </button>
            <AppButton text="Реєстрація" isBold />
          </div>
        </ul>
      </div>
    </div>
  </header>
</template>

<script setup>
import AppButton from '@/components/atoms/buttons/AppButton.vue';
import { ref } from 'vue';
import BurgerIconVue from '@/components/icons/BurgerIcon.vue';

const headerLinks = ref([
  { label: 'Волонтерам', url: '/' },
  { label: 'Замовникам', url: '/' },
  { label: 'Пропозиції', url: '/' },
]);
const isDropdownOpen = ref(false);
const toggleDropdown = () => {
  isDropdownOpen.value = !isDropdownOpen.value;
};
</script>
