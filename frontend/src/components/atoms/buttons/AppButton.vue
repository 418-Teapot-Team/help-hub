<template>
  <button
    class="w-full h-full p-2 font-semibold bg-primary bg-opacity-85 text-xl text-white"
    :type="type"
    @click="onClick"
  >
    {{ text }}
  </button>
</template>

<script>
export default {
  name: 'AppButton',
  props: ['text', 'type'],
  methods: {
    onClick() {
      this.$emit('onClick');
    },
  },
};
</script>
