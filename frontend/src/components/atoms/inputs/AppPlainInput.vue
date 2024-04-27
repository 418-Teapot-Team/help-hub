<template>
  <div class="flex flex-col justify-center items-start gap-y-1 w-full">
    <label class="">{{ label }}</label>
    <vee-field
      :type="type"
      class="px-2 py-1 border border-solid border-simple-gray/20 focus:border-primary w-full"
      :name="name"
      :placeholder="label"
    />
    <ErrorMessage :name="name" class="text-red-500 text-xs" />
  </div>
</template>
<script setup>
defineProps(['label', 'type', 'name']);
</script>
