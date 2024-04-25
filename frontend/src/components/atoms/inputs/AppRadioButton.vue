<template>
  <div class="flex justify-start items-center gap-x-2">
    <input
      type="radio"
      :name="name"
      :value="value"
      v-model="model"
      class="relative float-left -ms-[1.5rem] me-1 mt-0.5 h-5 w-5 appearance-none border border-solid border-black/20 before:pointer-events-none before:absolute before:h-4 before:w-4 before:bg-transparent before:opacity-0 before:shadow-checkbox before:shadow-transparent before:content-[''] after:absolute after:z-[1] after:block after:h-4 after:w-4 after:content-[''] checked:border-primary checked:before:opacity-[0.16] checked:after:absolute checked:after:left-1/2 checked:after:top-1/2 checked:after:h-[0.625rem] checked:after:w-[0.625rem] checked:after:border-primary checked:after:bg-primary checked:after:content-[''] checked:after:[transform:translate(-50%,-50%)] hover:cursor-pointer hover:before:opacity-[0.04] hover:before:shadow-black/20 focus:shadow-none focus:outline-none focus:ring-0 focus:before:opacity-[0.12] focus:before:shadow-black/60 focus:before:transition-[box-shadow_0.2s,transform_0.2s] checked:focus:border-primary checked:focus:before:shadow-checkbox checked:focus:before:transition-[box-shadow_0.2s,transform_0.2s] rtl:float-right"
    />
    <label>{{ label }}</label>
  </div>
</template>
<script setup>
defineProps(['name', 'value', 'label']);
const model = defineModel();
</script>
