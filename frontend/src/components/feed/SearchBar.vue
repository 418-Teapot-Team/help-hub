<template>
  <section>
    <div class="flex justify-center w-full px-6">
      <!-- TODO: add debounce for search-->
      <div class="border-2 border-primary bg-white rounded mr-2 w-full p-2">
        <input
          v-model="searchTerm"
          type="text"
          placeholder="Search volunteers..."
          class="rounded w-full"
        />
      </div>
      <!-- TODO: send the search request to server -->
      <AppButton
        text="Пошук"
        isBold
        @click="search"
        class="bg-primary hover:bg-primary-dark text-white py-2 px-4"
      />
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import AppButton from '@/components/atoms/buttons/AppButton.vue';
const searchTerm = ref('');
</script>

<style lang="scss" scoped></style>
