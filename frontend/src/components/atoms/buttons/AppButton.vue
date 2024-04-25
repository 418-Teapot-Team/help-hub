<template>
  <button
    :class="{
      'w-full h-full p-2 font-semibold text-xl': true,
      'bg-primary bg-opacity-85 text-white': buttonStyle === 'default',
      'bg-transparent border border-primary text-primary': buttonStyle === 'outline',
    }"
    :type="type"
    @click="onClick"
  >
    {{ text }}
  </button>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  text: String,
  type: {
    type: String,
    default: 'button',
  },
  buttonStyle: {
    type: String,
    default: 'default',
  },
});

const { emit } = defineEmits(['onClick']);

const onClick = () => {
  emit('onClick');
};
</script>
<script>
export default {
  name: 'AppButton',
};
</script>
