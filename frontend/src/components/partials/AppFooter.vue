<template>
  <footer class="fixed bottom-0 left-0 w-full bg-gray-800 mt-4">
    <div class="p-4 md:py-8">
      <div
        class="flex flex-col md:flex-row items-center justify-center md:justify-between lg:justify-center"
      >
        <img src="" alt="Our img is gonna be here" class="h-8 text-white" />
        <!-- Display single column list when screen is not small -->
        <ul class="flex-wrap items-center justify-center md:justify-end text-white sm:flex hidden">
          <li v-for="(link, index) in footerLinks" :key="index">
            <router-link :to="link.url" class="mx-5 hover:underline">{{ link.label }}</router-link>
          </li>
        </ul>
        <!-- Display two column lists when screen is small -->
        <div class="flex justify-between sm:hidden">
          <ul class="flex flex-col items-center justify-center text-white">
            <li v-for="(link, index) in firstColumn" :key="'firstColumn-' + index" class="mb-2">
              <router-link :to="link.url" class="mx-5 hover:underline">{{
                link.label
              }}</router-link>
            </li>
          </ul>
          <ul class="flex flex-col items-center justify-center text-white">
            <li v-for="(link, index) in secondColumn" :key="'secondColumn-' + index" class="mb-2">
              <router-link :to="link.url" class="mx-5 hover:underline">{{
                link.label
              }}</router-link>
            </li>
          </ul>
        </div>
      </div>
      <hr class="my-3 sm:my-6 mx-auto border-gray-700 lg:my-8" />
      <span class="block text-sm text-gray-400 text-center"
        >© 2024 Teapot418. All Rights Reserved.</span
      >
    </div>
  </footer>
</template>

<script setup>
import { ref, computed } from 'vue';

const footerLinks = ref([
  { label: 'Propositions', url: '/' },
  { label: 'Volunteers', url: '/' },
  { label: 'Volunteers', url: '/' },
  { label: 'Volunteers', url: '/' },
]);

const halfIndex = Math.ceil(footerLinks.value.length / 2);
const firstColumn = computed(() => footerLinks.value.slice(0, halfIndex));
const secondColumn = computed(() => footerLinks.value.slice(halfIndex));
</script>
