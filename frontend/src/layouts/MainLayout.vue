<template>
  <AppHeaderVue />
  <div class="w-full h-10 flex justify-center"></div>

  <main>
    <router-view />
  </main>
</template>

<script setup>
import AppHeaderVue from '@/components/AppHeader.vue';
</script>
