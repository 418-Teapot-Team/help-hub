<template>
  <div class="flex justify-center">
    <div v-for="(card, index) in cards" :key="index">
      <StatCard :stat="card.stat" :label="card.label" />
    </div>
  </div>
</template>

<script setup>
import StatCard from '@/components/home/stats/StatCard.vue';
import { ref } from 'vue';

const cards = ref([
  { label: 'bahato', stat: 1278 },
  { label: 'bilshe', stat: 12738 },
  { label: 'dohyja', stat: 9087298 },
]);
</script>
