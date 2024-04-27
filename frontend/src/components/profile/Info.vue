<template>
  <div
    class="relative w-full lg:max-h-[calc(100vh-144px) h-full border border-black/10 shadow-sm px-8 py-4 flex flex-col justify-start items-center gap-y-4 overflow-auto"
  >
    <div class="w-full flex justify-start items-center">
      <span class="text-xl font-semibold">Редагування профілю</span>
    </div>
    <div class="flex justify-center items-center w-full h-full">
      <vee-form
        :validation-schema="schema"
        :initial-values="formValues"
        class="w-full flex flex-col justify-between h-full gap-y-6 lg:gap-y-0"
        @submit="onSubmit"
      >
        <div class="flex flex-col gap-y-4 lg:flex-row justify-center items-start gap-x-4 w-full">
          <div class="flex flex-col justify-start items-start gap-y-4 w-full">
            <span class="text-lg underline">Персональні данні</span>
            <AppPlainInput type="text" label="Ім'я*" name="name" />
            <AppPhoneInput label="Телефон*" />
            <AppPlainInput type="email" label="E-mailі*" name="email" />
          </div>
          <div class="flex flex-col justify-start items-start gap-y-4 w-full">
            <span class="text-lg underline">Соц. мережі</span>
            <AppPlainInput type="text" label="Telegram" name="telegram" class="w-full" />
            <AppPlainInput type="text" label="Facebook" name="facebook" class="w-full" />
            <AppPlainInput type="text" label="Twitter" name="twitter" class="w-full" />
            <AppPlainInput type="text" label="Instagram" name="instagram" class="w-full" />
          </div>
        </div>
        <div class="w-full">
          <AppButton class="mb-6 lg:mb-0" type="submit" text="Зберегти" is-bold />
        </div>
      </vee-form>
    </div>
  </div>
</template>

<script setup>
import AppPlainInput from '@/components/atoms/inputs/AppPlainInput.vue';
import AppPhoneInput from '@/components/atoms/inputs/AppPhoneInput.vue';
import AppButton from '../atoms/buttons/AppButton.vue';
import { reactive } from 'vue';
import { ref } from 'vue';

const schema = reactive({
  name: 'required|min:3|max:150',
  email: 'required|email|min:3|max:100',
  phone: 'required|min:10|max:18',
});

const formValues = ref({
  name: 'Нестор Петрович',
  email: 'letopisec@gmail.com',
  phone: '0677777777',
  facebook: 'https://www.facebook.com/profile/834294',
  telegram: '@letopis_top123',
  instagram: '@from_900_year',
});

function onSubmit(values) {
  console.log(values);
}
</script>
