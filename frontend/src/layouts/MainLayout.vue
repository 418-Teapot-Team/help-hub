<template>
  <AppHeaderVue />
  <main>
    <router-view />
  </main>
  <AppFooter />
  <Registration v-if="isRegisterPopupOpen" />
  <Login v-if="isLoginPopupOpen" />
  <CreateRequest v-if="isCreateOpen" />
</template>

<script setup>
import { useAuthStore } from '@/stores/auth';
import AppFooter from '@/components/partials/AppFooter.vue';
import AppHeaderVue from '@/components/partials/AppHeader.vue';
import Registration from '@/components/modals/Registration.vue';
import CreateRequest from '@/components/modals/CreateRequest.vue';
import Login from '@/components/modals/Login.vue';
import { computed, onBeforeMount } from 'vue';
import { AUTH_TOKEN_KEY } from '@/utils/constants';
import { useRequestsStore } from '@/stores/requests';

const auhtStore = useAuthStore();
const requestsStore = useRequestsStore();

onBeforeMount(() => {
  if (localStorage.getItem(AUTH_TOKEN_KEY)) {
    auhtStore.whoAmI();
  }
});

const isRegisterPopupOpen = computed(() => auhtStore.isRegisterPopupOpen);
const isLoginPopupOpen = computed(() => auhtStore.isLoginPopupOpen);
const isCreateOpen = computed(() => requestsStore.isCreateOpen);
</script>
