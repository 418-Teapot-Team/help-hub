<template>
  <section>
    <div class="flex justify-center">
      <!-- TODO: add debounce for search-->
      <div class="border-2 border-primary bg-white rounded mr-2 w-3/5">
        <input
          v-model="searchTerm"
          type="text"
          placeholder="Search volunteers..."
          class="m-2 rounded"
        />
      </div>
      <!-- TODO: send the search request to server -->
      <button
        @click="search"
        class="bg-primary hover:bg-primary-dark text-white font-bold py-2 px-4 rounded"
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
