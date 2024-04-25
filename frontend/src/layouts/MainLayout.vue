<template>
  <AppHeaderVue />
  <main class="min-h-screen">
    <router-view />
  </main>
  <AppFooter />
</template>

<script setup>
import AppFooter from '@/components/partials/AppFooter.vue';
import AppHeaderVue from '@/components/partials/AppHeader.vue';
</script>
