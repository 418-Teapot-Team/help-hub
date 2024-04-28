<template>
  <section
    id="profile"
    class="px-8 md:px-16 py-8 min-h-[calc(100vh-80px)] md:min-h-0 md:h-[calc(100vh-80px)] h-full overflow-auto"
  >
    <div
      class="flex flex-col items-center md:flex-row justify-center md:items-start h-full gap-x-0 gap-y-8 md:gap-y-0 md:gap-x-8"
    >
      <div class="flex flex-col justify-start gap-y-8 h-full w-full md:w-fit">
        <Avatar @onAvatarChange="isFilePopupOpen = true" :editable="true" />
        <Stats :profileData="profileData" />
      </div>
      <div class="w-full h-full">
        <Info :profileData="profileData" />
      </div>
    </div>

    <DragFile v-if="isFilePopupOpen" @closeModal="isFilePopupOpen = false" @onUpload="uploadFile" />
    <div
      v-if="isLoading"
      class="flex fixed justify-center items-center top-0 left-0 right-0 bottom-0 z-30"
    >
      <div class="fixed top-0 left-0 right-0 bottom-0 bg-white/50 z-40"></div>
      <Spinner class="z-50" />
    </div>
  </section>
</template>
<script setup>
import DragFile from '@/components/modals/DragFile.vue';
import Avatar from '@/components/profile/Avatar.vue';
import Info from '@/components/profile/Info.vue';
import Spinner from '@/components/atoms/Spinner.vue';
import { onBeforeMount, ref } from 'vue';
import Stats from '@/components/profile/Stats.vue';
import { useProfileStore } from '@/stores/profile';
import { AUTH_TOKEN_KEY } from '@/utils/constants';

const profileStore = useProfileStore();
const profileData = ref({});

onBeforeMount(() => {
  if (localStorage.getItem(AUTH_TOKEN_KEY)) {
    profileStore.getMe().then((res) => {
      profileData.value = res;
    });
  }
});

const isFilePopupOpen = ref(false);
const isLoading = ref(false);

function uploadFile(file) {
  isLoading.value = true;
  setTimeout(() => {
    isFilePopupOpen.value = false;
    isLoading.value = false;
    console.log(file);
  }, 1500);
}
</script>
