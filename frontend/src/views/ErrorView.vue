<template>
  <section
    id="not_found"
    class="w-screen h-screen flex flex-col gap-y-4 justify-center items-center"
  >
    <img class="w-20 h-10" src="/public/images/HandToHandLogo.webp" />
    <h1 class="text-8xl sm:text-[248px] font-semibold text-primary">404</h1>
    <div class="flex flex-col justify-start items-center">
      <p class="text-gray-500">Page you are looking for is nout found.</p>
      <p class="text-gray-500">Please return to home page.</p>
    </div>

    <AppButton type="button" @on-click="goHome" text="Homepage" is-bold />
  </section>
</template>
<script setup>
import AppButton from '@/components/atoms/buttons/AppButton.vue';
import { useRouter } from 'vue-router';

const router = useRouter();

function goHome() {
  router.push('/');
}
</script>
