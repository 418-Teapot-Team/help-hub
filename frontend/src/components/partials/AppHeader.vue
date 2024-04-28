<template>
  <header class="h-20 px-4 py-2 flex items-center justify-between shadow-md">
    <div class="flex items-center">
      <img src="/images/HandToHandLogo.webp" class="object-contain w-20" />
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
      <div :class="logged ? 'hidden' : 'md:flex hidden justify-center items-center gap-x-6'">
        <button class="px-3 py-2" @click="openLoginPopup">
          <span class="font-semibold hover:underline">Вхід</span>
        </button>
        <AppButton text="Реєстрація" @onClick="openRegisterPopup" isBold />
      </div>
      <div :class="logged ? 'hidden md:flex flex-row items-center gap-x-4' : 'hidden'">
        <div class="flex flex-col items-center">
          <span class="font-bold text-white bg-primary p-1 text-center">{{ full_name }} </span>
          <span v-if="volunteer" class="text-dark-text">Volunteer</span>
        </div>
        <img class="w-14" src="/images/Profile.png" alt="" />
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
          <div :class="logged ? 'hidden' : 'p-4 flex justify-end w-full'">
            <button class="px-3 py-2" @click="openLoginPopup">
              <span class="font-semibold hover:underline">Вхід</span>
            </button>
            <AppButton text="Реєстрація" @onClick="openRegisterPopup" isBold />
          </div>
          <div :class="logged ? 'w-full text-end px-6 py-4' : 'hidden'">
            <span class="font-bold text-white bg-primary p-2 text-center">{{ full_name }} </span>
            <span v-if="volunteer" class="text-dark-text pl-6">Volunteer</span>
          </div>
        </ul>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores/auth';
import BurgerIconVue from '../icons/BurgerIcon.vue';
const authStore = useAuthStore();
import AppButton from '@/components/atoms/buttons/AppButton.vue';

const full_name = ref('Pidaras Pidrilovich');
const volunteer = ref(true);
const logged = ref(false);

const headerLinks = ref([
  { label: 'Волонтерам', url: '/' },
  { label: 'Замовникам', url: '/' },
  { label: 'Пропозиції', url: '/' },
]);
const isDropdownOpen = ref(false);
const toggleDropdown = () => {
  isDropdownOpen.value = !isDropdownOpen.value;
};

function openRegisterPopup() {
  authStore.setRegisterPopupOpenStatus(true);
}
function openLoginPopup() {
  authStore.setLoginPopupOpenStatus(true);
}
</script>
