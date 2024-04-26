<template>
  <section class="py-9 bg-section-secondary">
    <div class="flex mx-auto font-semibold text-3xl justify-center py-4 bg-inherit">
      <span>Трішки статистики</span>
    </div>
    <div class="flex flex-wrap justify-center bg-inherit">
      <div v-for="(card, index) in cards" :key="index">
        <StatCard :stat="card.stat" :label="card.label" :image="card.image" />
      </div>
    </div>

    <div class="flex mx-auto text-lg justify-center py-4 bg-inherit w-1/2 text-center mt-2">
      <span
        >Hand to Hand створена щоб усі могли знайти допомого або ж проявити себе та допомогти іншим,
        тому ми сподіваємося, що наведена статистика буде невпинно зростати.</span
      >
    </div>
  </section>
</template>

<script setup>
import StatCard from '@/components/home/stats/StatCard.vue';
import { ref } from 'vue';

const cards = ref([
  { label: 'Заявок', stat: '10564', image: '/images/Resume.png' },
  { label: 'Волонтерів', stat: '1298', image: '/images/HandUp.png' },
  { label: 'Виконаних завдань', stat: '8754', image: '/images/Success.png' },
]);
</script>
