<template>
  <footer class="w-full bg-simple-gray pt-4">
    <div class="p-4 md:py-8">
      <div
        class="flex flex-col md:flex-row items-center justify-center md:justify-between lg:justify-center"
      >
        <router-link to="/">
          <img src="/images/HandToHandLogoLight.webp" alt="" class="h-8 text-white mb-5 md:mb-0" />
        </router-link>
        <!-- Display single row list when screen is not small -->
        <ul class="flex-wrap items-center justify-center md:justify-end text-white sm:flex hidden">
          <li v-for="(link, index) in footerLinks" :key="index">
            <router-link :to="link.url" class="mx-5 hover:underline">{{ link.label }}</router-link>
          </li>
          <li>
            <div :class="logged ? 'hidden' : ''">
              <button class="mx-5" @click="openLoginPopup">
                <span class="hover:underline">Вхід</span>
              </button>
              <button class="mx-5" @click="openRegisterPopup">
                <span class="hover:underline">Реєстрація</span>
              </button>
            </div>
            <div :class="logged ? 'w-full text-end px-12 pb-2' : 'hidden'">
              Welcome,
              <span v-if="volunteer" class="uppercase font-bold text-light-text pl-6"
                >volunteer</span
              >
            </div>
          </li>
        </ul>
        <!-- Display two column lists when screen is small -->
        <div class="flex justify-between sm:hidden">
          <ul
            class="grid grid-cols-2 gap-x-9 gap-y-3 flex-wrap items-center justify-center md:justify-end text-white"
          >
            <li v-for="(link, index) in footerLinks" :key="index">
              <router-link :to="link.url" class="mx-5 hover:underline">{{
                link.label
              }}</router-link>
            </li>
          </ul>
        </div>
      </div>
      <hr class="my-3 sm:my-6 mx-auto border-gray-700 lg:my-8" />
      <span class="block text-sm text-gray-400 text-center"
        >© 2024 Teapot418. All Rights Reserved.</span
      >
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores/auth';
const authStore = useAuthStore();

const footerLinks = ref([
  { label: 'Волонтеру', url: '/requests' },
  { label: 'Шукачу', url: '/findvolunteer' },
]);

function openRegisterPopup() {
  authStore.setRegisterPopupOpenStatus(true);
}

function openLoginPopup() {
  authStore.setLoginPopupOpenStatus(true);
}
</script>
