<template>
  <button
    :class="{
      'w-fit h-fit py-2 px-4 text-xl hover:bg-simple-gray transition ease-out duration-200': true,
      'bg-primary bg-opacity-85 text-white': buttonStyle === 'default',
      'bg-transparent border-2 border-solid border-primary text-primary': buttonStyle === 'outline',
      'font-semibold': isBold,
    }"
    :type="type"
    @click="onClick"
  >
    {{ text }}
  </button>
</template>

<script setup>
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
