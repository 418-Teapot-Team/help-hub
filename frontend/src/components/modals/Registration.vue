<template>
  <Teleport to="#app">
    <div
      class="fixed top-0 left-0 right-0 bottom-0 z-10 bg-black/20 flex justify-center items-center"
      @click="closeModal"
    >
      <vee-form
        :validation-schema="schema"
        @submit="onSubmit"
        class="relative z-20 w-[320px] xs:w-[380px] sm:w-[420px] md:w-[480px] lg:w-[540px] h-fit bg-white shadow-sm px-6 py-6 flex flex-col justify-start items-center gap-y-6 max-h-screen overflow-y-auto"
        @click.stop
      >
        <div @click="closeModal" class="absolute right-4 top-4 cursor-pointer hover:stroke-primary">
          <CloseIcon class="w-6 h-6" />
        </div>
        <h1 class="font-semibold text-2xl">Реєстрація</h1>
        <div class="w-full flex flex-col justify-center gap-y-2">
          <AppPlainInput type="text" label="Ім'я*" name="name" />
          <AppPhoneInput label="Телефон*" />
          <AppPlainInput type="email" label="E-mailі*" name="email" />
          <AppPlainInput type="password" label="Пароль*" name="password" />
          <AppPlainInput type="password" label="Підтвердження паролю*" name="password_confirm" />
          <div class="pt-2 flex flex-col justify-start items-start gap-y-2">
            <AppRadioButton
              v-for="item in accountTypes"
              v-model="accountType"
              :key="'choice_' + item.value"
              :label="item.label"
              :value="item.value"
            />
          </div>
        </div>
        <div class="w-full flex flex-col justify-start items-center gap-y-2">
          <AppButton class="w-full" type="submit" text="Далі" is-bold />
          <span
            >Уже зареєстровані?
            <span class="font-semibold text-primary cursor-pointer" @click="goToLogin"
              >Увійти</span
            ></span
          >
        </div>
      </vee-form>
    </div>
  </Teleport>
</template>
<script setup>
import { reactive, ref } from 'vue';
import { useAuthStore } from '@/stores/auth';
import AppButton from '@/components/atoms/buttons/AppButton.vue';
import AppPlainInput from '@/components/atoms/inputs/AppPlainInput.vue';
import AppPhoneInput from '@/components/atoms/inputs/AppPhoneInput.vue';
import CloseIcon from '@/components/icons/CloseIcon.vue';
import AppRadioButton from '@/components/atoms/inputs/AppRadioButton.vue';

const emit = defineEmits(['onSubmit']);

const authStore = useAuthStore();

const accountTypes = ref([
  {
    label: 'Потребую допомоги',
    value: 'requestor',
  },
  {
    label: 'Хочу стати волонтером',
    value: 'volunteer',
  },
]);

const accountType = ref('requestor');

const schema = reactive({
  name: 'required|min:3|max:150',
  email: 'required|email|min:3|max:100',
  phone: 'required|min:10|max:18',
  password: 'required|min:6|max:100',
  password_confirm: 'required|passwords_mismatch:@password',
});

function onSubmit(values) {
  emit('onSubmit');
  console.log({
    values,
    account_type: accountType.value,
  });
}

function closeModal() {
  authStore.setRegisterPopupOpenStatus(false);
}

function goToLogin() {
  authStore.setRegisterPopupOpenStatus(false);
  authStore.setLoginPopupOpenStatus(true);
}
</script>
