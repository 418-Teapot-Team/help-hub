<template>
  <header class="h-20 px-8 py-2 flex items-center justify-between shadow-md">
    <div class="flex items-center">
      <img src="/images/HandToHandLogo.webp" class="object-contain w-20" />
    </div>
    <ul class="hidden md:flex flex-1 justify-center gap-x-10">
      <li v-for="(item, idx) in headerLinks" :key="idx" class="text-dark-text text-lg">
        <router-link :to="item.url">
          {{ item.label }}
        </router-link>
      </li>
    </ul>
    <div>
      <div class="flex justify-center items-center gap-x-6">
        <button class="px-3 py-2"><span class="font-semibold">Вхід</span></button>
        <AppButton text="Реєстрація" isBold />
      </div>
    </div>
  </header>
</template>

<script setup>
import AppButton from '@/components/atoms/buttons/AppButton.vue';
import { ref } from 'vue';

const headerLinks = ref([
  { label: 'Волонтерам', url: '/' },
  { label: 'Замовникам', url: '/' },
  { label: 'Пропозиції', url: '/' },
]);
</script>
