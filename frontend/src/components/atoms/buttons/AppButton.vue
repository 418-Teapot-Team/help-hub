<template>
  <button
    :class="{
      'w-fit h-fit py-2 px-4 text-xl  transition ease-out duration-200': true,
      'bg-primary hover:bg-simple-gray text-white': buttonStyle === 'default',
      'bg-transparent border-2 border-solid border-primary text-primary hover:bg-primary hover:text-white':
        buttonStyle === 'outline',
      'font-semibold': isBold,
    }"
    :type="type"
    @click="onClick"
  >
    {{ text }}
  </button>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

defineProps({
  text: String,
  type: {
    type: String,
    default: 'button',
  },
  buttonStyle: {
    type: String,
    default: 'default',
  },
  isBold: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits(['onClick']);

function onClick() {
  emit('onClick');
}
</script>
<script>
export default {
  name: 'AppButton',
};
</script>
