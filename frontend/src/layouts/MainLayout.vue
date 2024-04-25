<template>
  <main>
    <h1>Main!</h1>
    <AppButton :text="'Primary'" />
    <AppButton :text="'Secondary'" :buttonStyle="'outline'" />
    <router-view />
  </main>
</template>

<script setup>
import { defineProps } from 'vue';
import AppButton from '@/components/atoms/buttons/AppButton.vue';

const props = defineProps({
  text: String,
  buttonStyle: {
    type: String,
    default: '',
  },
});
</script>
