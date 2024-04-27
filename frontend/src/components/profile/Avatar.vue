<template>
  <div
    class="relative w-full md:w-[240px] h-[240px] border border-black/10 shadow-sm px-8 py-4 pt-1 flex flex-col justify-center items-center gap-y-4"
  >
    <span class="text-xl font-semibold">Аватар</span>
    <div
      class="border rounded-full overflow-hidden w-[150px] h-[150px] flex items-center justify-center bg-white"
    >
      <img src="/images/howWorkImg.webp" width="150" height="150" />
    </div>
    <div class="absolute right-2 bottom-2 cursor-pointer">
      <EditIcon class="w-6 h-6" @click="onAvatarChange" />
    </div>
  </div>
</template>

<script setup>
import EditIcon from '@/components/icons/EditIcon.vue';

const emit = defineEmits(['onAvatarChange']);

function onAvatarChange() {
  emit('onAvatarChange');
}
</script>
