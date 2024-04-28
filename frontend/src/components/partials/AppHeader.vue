<template>
  <header class="h-20 px-4 py-2 flex items-center justify-between shadow-md">
    <div
      class="absolute mt-[620px] md:mt-48 z-50 bg-white w-[157px] h-contain md:flex justify-center shadow-sm right-0"
      v-if="isProfileOpen"
    >
      <div class="flex flex-col text-2xl text-center text-dark-text">
        <router-link :to="profileUrl" class="py-6">
          <span class="text-3xl font-semibold">Profile</span>
        </router-link>
        <router-link :to="requestUrl" v-if="volunteer === 'requestor'">Create request</router-link>
        <router-link :to="applyUrl" v-if="volunteer === 'volunteer'">View request</router-link>
        <div class="bottom-0 pb-3 text-center">
          <button @click="handleSignOut">
            <span class="border-t-2 text-red-700 font-semibold">Logout</span>
          </button>
        </div>
      </div>
    </div>
    <div class="flex items-center">
      <router-link to="/">
        <img src="/images/HandToHandLogo.webp" class="object-contain w-20" />
      </router-link>
    </div>
    <ul class="hidden md:flex flex-1 justify-center gap-x-10">
      <li
        v-for="(item, idx) in headerLinks"
        :key="idx"
        class="text-dark-text text-lg hover:underline"
      >
        <router-link :to="item.url">
          {{ item.label }}
        </router-link>
      </li>
    </ul>
    <div>
      <div :class="isLoggedIn ? 'hidden' : 'md:flex hidden justify-center items-center gap-x-6'">
        <button class="px-3 py-2" @click="openLoginPopup">
          <span class="font-semibold hover:underline">Вхід</span>
        </button>
        <AppButton text="Реєстрація" @onClick="openRegisterPopup" isBold />
      </div>
      <div :class="isLoggedIn ? 'hidden md:flex flex-row items-center gap-x-4' : 'hidden'">
        <div class="flex flex-col items-center">
          <span class="font-bold text-white bg-primary p-1 text-center"
            >{{ profileData.full_name }}
          </span>
          <span v-if="volunteer" class="text-dark-text">Volunteer</span>
        </div>
        <button @click="openProfileDropdown">
          <img class="w-14" src="/images/Profile.png" alt="" />
        </button>
      </div>

      <BurgerIconVue @click="toggleDropdown" class="object-contain w-10 md:hidden" />

      <div v-if="isDropdownOpen" class="flex flex-col">
        <ul
          class="absolute z-10 w-full flex flex-col items-start top-20 right-0 bg-white shadow-md md:hidden"
        >
          <li
            v-for="(item, idx) in headerLinks"
            :key="idx"
            class="text-dark-text text-xl w-full h-full px-4 py-2 hover:bg-primary"
          >
            <router-link :to="item.url">
              {{ item.label }}
            </router-link>
          </li>
          <div :class="isLoggedIn ? 'hidden' : 'p-4 flex justify-end w-full'">
            <button class="px-3 py-2" @click="openLoginPopup">
              <span class="font-semibold hover:underline">Вхід</span>
            </button>
            <AppButton text="Реєстрація" @onClick="openRegisterPopup" isBold />
          </div>
          <div
            :class="
              isLoggedIn ? 'w-full flex items-center justify-end text-center px-6 py-4' : 'hidden'
            "
          >
            <span class="font-bold text-white bg-primary p-2 text-center"
              >{{ profileData.full_name }}
            </span>
            <span v-if="volunteer" class="text-dark-text pl-6 pr-6">Volunteer</span>
            <button @click="openProfileDropdown">
              <img class="w-11 md:w-14" src="/images/Profile.png" alt="" />
            </button>
          </div>
        </ul>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';

import BurgerIconVue from '../icons/BurgerIcon.vue';
const authStore = useAuthStore();
import AppButton from '@/components/atoms/buttons/AppButton.vue';

const isLoggedIn = computed(() => authStore.isLoggedIn);
const profileData = computed(() => authStore.profileData);

const volunteer = computed(() => authStore.profileData.role);
console.log(volunteer);

const router = useRouter();

function handleSignOut() {
  authStore.signOut();
  router.push('/');
}

const requestUrl = '/my-requests';
const applyUrl = '/my-applies';
const profileUrl = '/me';

const headerLinks = ref([
  { label: 'Волонтеру', url: '/requests' },
  { label: 'Шукачу', url: '/findvolunteer' },
]);
const isDropdownOpen = ref(false);
const toggleDropdown = () => {
  isDropdownOpen.value = !isDropdownOpen.value;
};
const isProfileOpen = ref(false);

const openProfileDropdown = () => {
  isProfileOpen.value = !isProfileOpen.value;
};

function openRegisterPopup() {
  authStore.setRegisterPopupOpenStatus(true);
}
function openLoginPopup() {
  authStore.setLoginPopupOpenStatus(true);
}
</script>
