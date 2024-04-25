<template>
  <AppHeaderVue />
  <main>
    <router-view />
  </main>
  <AppFooter />
</template>

<script setup>
import AppFooter from '@/components/partials/AppFooter.vue';
import AppHeaderVue from '@/components/partials/AppHeader.vue';
</script>
