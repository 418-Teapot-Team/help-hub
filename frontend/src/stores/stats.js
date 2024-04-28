// stats.js
import { defineStore } from 'pinia';
import { ref } from 'vue';

const api = import.meta.env.VITE_BASE_API;

export const useStatsStore = defineStore('statsStore', () => {
  const data = ref([]);

  async function fetchStats() {
    const response = await fetch(api + '/stats/general');
    if (response.ok) {
      this.stats = await response.json();
    } else {
      console.error('HTTP-Error: ' + response.status);
    }
  }

  return {
    data,
    fetchStats,
  };
});
