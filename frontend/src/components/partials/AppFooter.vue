<template>
  <footer class="fixed bottom-0 left-0 w-full shadow bg-gray-800 mb-4">
    <div class="w-full max-w-screen-xl mx-auto p-4 md:py-8">
      <div class="flex items-center justify-center">
        <ul class="flex flex-wrap items-center justify-center dark:text-white">
          <li>
            <span class="flex items-center mb-4 sm:mb-0 space-x-3 rtl:space-x-reverse me-5">
              <img src="" alt="Our img is gonna be here" class="h-8" />
              <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white"
                >Teapot418</span
              >
            </span>
          </li>
          <li v-for="(link, index) in footerLinks" :key="index">
            <router-link :to="link.url" class="me-4 hover:underline md:me-6">{{
              link.label
            }}</router-link>
          </li>
        </ul>
      </div>
      <hr class="my-6 mx-auto border-gray-700 lg:my-8" />
      <span class="block text-sm text-gray-400 sm:text-center"
        >© 2024 Teapot418. All Rights Reserved.</span
      >
    </div>
  </footer>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const footerLinks = ref([
      { label: 'Propositions', url: '/' },
      { label: 'Volunteers', url: '/' },
      { label: 'Volunteers', url: '/' },
      { label: 'Volunteers', url: '/' },
    ]);

    return {
      footerLinks,
    };
  },
};
</script>
