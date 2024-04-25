<template>
  <AppHeaderVue />
  <main class="min-h-screen">
    <router-view />
  </main>
  <AppFooter />
  <Registration v-if="isRegisterPopupOpen" />
  <Login v-if="isLoginPopupOpen" />
</template>

<script setup>
import { useAuthStore } from '@/stores/auth';
import AppFooter from '@/components/partials/AppFooter.vue';
import AppHeaderVue from '@/components/partials/AppHeader.vue';
import Registration from '@/components/modals/Registration.vue';
import Login from '@/components/modals/Login.vue';
import { computed } from 'vue';

const auhtStore = useAuthStore();

const isRegisterPopupOpen = computed(() => auhtStore.isRegisterPopupOpen);
const isLoginPopupOpen = computed(() => auhtStore.isLoginPopupOpen);
</script>
