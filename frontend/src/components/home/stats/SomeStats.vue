<template>
  <section>
    <div class="bg-section-secondary h-[calc(100vh)] py-1">
      <div class="flex justify-center sm:mt-32 lg:mt-28 2xl:mt-20">
        <span class="text-dark-text text-4xl md:text-5xl font-semibold">Трішки статистики</span>
      </div>
      <div class="flex flex-wrap justify-center bg-inherit mt-9">
        <div v-for="(card, index) in cards" :key="index">
          <StatCard :stat="card.stat" :label="card.label" :image="card.image" />
        </div>
      </div>

      <div
        class="flex mx-auto text-lg justify-center py-4 px-2 bg-inherit sm:w-3/4 text-center sm:mt-2"
      >
        <span class="font-semibold text-xl"
          >Hand to Hand створена щоб усі могли знайти допомого або ж проявити себе та допомогти
          іншим, тому ми сподіваємося, що наведена статистика буде невпинно зростати.</span
        >
      </div>
    </div>
  </section>
</template>

<script setup>
import StatCard from '@/components/home/stats/StatCard.vue';
import { ref, onMounted } from 'vue';
// import { useStatsStore } from '@/stores/stats.js';

// const store = useStatsStore();

onMounted(async () => {
  // await store.fetchStats();
  // console.log(store.data)
});

const cards = ref([
  { label: 'Заявок', stat: '10564', image: '/images/Resume.png' },
  { label: 'Волонтерів', stat: '1298', image: '/images/HandUp.png' },
  { label: 'Виконаних завдань', stat: '8754', image: '/images/Success.png' },
]);
</script>
