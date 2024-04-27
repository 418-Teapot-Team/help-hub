<template>
  <div
    class="relative w-full md:w-[240px] h-full border border-black/10 shadow-sm px-8 py-4 flex flex-col justify-start items-start md:items-center gap-y-4"
  >
    <span class="text-xl font-semibold">Статистика</span>
    <div>
      <ul class="flex flex-col justify-start items-start gap-y-3">
        <li
          v-for="(item, idx) in statsData"
          :key="idx"
          class="flex flex-col justify-center gap-y-1"
        >
          <span class="text-base">{{ item.title }}:</span>
          <span class="text-primary font-semibold">{{ item.value }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const statsData = ref([
  { title: 'Успішних допомог', value: '125' },
  { title: 'Найбільше допоміг у категорії', value: 'Продукти харчування' },
  { title: 'Рівент волонтера', value: 'Помагатор' },
  { title: 'На сайті з', value: '20.04.2024' },
]);
</script>
