<template>
  <AppHeaderVue />
  <main>
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
import { computed, onBeforeMount } from 'vue';
import { AUTH_TOKEN_KEY } from '@/utils/constants';

const auhtStore = useAuthStore();

onBeforeMount(() => {
  if (localStorage.getItem(AUTH_TOKEN_KEY)) {
    auhtStore.whoAmI();
  }
});

const isRegisterPopupOpen = computed(() => auhtStore.isRegisterPopupOpen);
const isLoginPopupOpen = computed(() => auhtStore.isLoginPopupOpen);
</script>
