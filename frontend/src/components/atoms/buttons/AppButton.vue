<template>
  <button
    :class="[
      'w-full h-full p-2 font-semibold text-xl',
      buttonStyle === 'default'
        ? 'bg-primary bg-opacity-85 text-white'
        : 'bg-transparent border border-primary text-primary',
    ]"
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
    default: 'primary',
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
