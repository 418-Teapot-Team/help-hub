<template>
  <AppHeaderVue />
  <div class="w-full h-10 flex justify-center"></div>

  <main>
    <router-view />
    <AppFooter />
  </main>
</template>

<script setup>
import AppFooter from '@/components/partials/AppFooter.vue';
import AppHeaderVue from '@/components/AppHeader.vue';
</script>
