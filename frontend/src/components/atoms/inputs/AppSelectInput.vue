<template>
  <div>
    <v-select
      class="input text-base bg-white border border-solid border-primary w-full min-h-[32px]"
      v-model="model"
      :options="options"
      :multiple="isMultiple ? isMultiple : false"
      :selectable="() => (max ? model.length < max : true)"
      :label="label"
      :reduce="(option) => option[`${dataKey}`]"
    />
  </div>
</template>
<script setup>
import { defineModel } from 'vue';

defineProps(['options', 'label', 'dataKey', 'isMultiple', 'max']);

const model = defineModel();
</script>
<style>
.vs__dropdown-toggle {
  border: 0px !important;
}
.input {
  --vs-controls-color: rgb(0, 0, 0);

  --vs-dropdown-bg: rgb(250 250 250);
  --vs-dropdown-color: rgb(250 250 250);
  --vs-dropdown-option-color: #000;

  --vs-selected-bg: #fff;
  --vs-selected-color: #000;

  --vs-search-input-color: #eeeeee;

  --vs-dropdown-option--active-bg: #eeeeee;
  --vs-dropdown-option--active-color: #000;
}
</style>
