<template>
  <div
    class="relative w-full md:w-[240px] h-[240px] border border-black/10 shadow-sm px-8 pb-4 flex flex-col justify-center items-center gap-y-4"
    :class="{
      'pt-1': editable,
      'pt-4': !editable,
    }"
  >
    <span class="text-xl font-semibold" v-if="editable">Аватар</span>
    <div
      class="border rounded-full overflow-hidden w-[150px] h-[150px] flex items-center justify-center bg-white"
    >
      <img src="/images/howWorkImg.webp" width="150" height="150" />
    </div>
    <div class="absolute right-2 bottom-2 cursor-pointer" v-if="editable">
      <EditIcon class="w-6 h-6" @click="onAvatarChange" />
    </div>
  </div>
</template>

<script setup>
import EditIcon from '@/components/icons/EditIcon.vue';

const props = defineProps({
  editable: {
    type: Boolean,
    default: true,
  },
});

const emit = defineEmits(['onAvatarChange']);

function onAvatarChange() {
  if (props.editable) {
    emit('onAvatarChange');
  }
}
</script>
