<template>
  <section>
    <div class="flex justify-center gap-2">
      <!-- TODO: add debounce for search-->
      <div class="border-2 border-primary bg-white w-full">
        <input v-model="searchTerm" type="text" placeholder="Search volunteers..." class="m-2" />
      </div>
      <!-- TODO: send the search request to server -->
      <button
        @click="search"
        class="bg-primary hover:bg-primary-dark text-white font-bold py-2 px-4"
      >
        Search
      </button>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const searchTerm = ref('');
</script>

<style lang="scss" scoped></style>
