<template>
  <Teleport to="#app">
    <div
      class="fixed top-0 left-0 right-0 bottom-0 z-10 bg-black/20 flex justify-center items-center max-h-screen overflow-y-auto"
      @click="closeModal"
    >
      <vee-form
        :validation-schema="schema"
        @submit="onSubmit"
        class="relative z-20 w-[320px] xs:w-[380px] sm:w-[420px] md:w-[480px] lg:w-[540px] h-fit bg-white shadow-sm px-6 py-6 flex flex-col justify-start items-center gap-y-6"
        @click.stop
      >
        <div @click="closeModal" class="absolute right-4 top-4 cursor-pointer hover:stroke-primary">
          <CloseIcon class="w-6 h-6" />
        </div>
        <h1 class="font-semibold text-2xl">Вхід</h1>
        <div class="w-full flex flex-col justify-center gap-y-2">
          <AppPhoneInput label="Телефон" />
          <AppPlainInput type="password" label="Пароль" name="password" />
          <AppCheckboxInput
            v-model="isVolunteer"
            name="is_volunteer"
            label="Увійти як волонтер"
            class="mt-2"
          />
        </div>
        <div class="w-full flex flex-col justify-start items-center gap-y-2">
          <AppButton class="w-full" type="submit" text="Далі" is-bold />
          <span
            >Вперше на нашому сайті?
            <span class="font-semibold text-primary cursor-pointer" @click="goToRegister"
              >Зареєструватись</span
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
import AppCheckboxInput from '@/components/atoms/inputs/AppCheckboxInput.vue';

const emit = defineEmits(['onSubmit']);

const authStore = useAuthStore();

const schema = reactive({
  phone: 'required|min:10|max:18',
  password: 'required|min:6|max:100',
});

const isVolunteer = ref(false);

function onSubmit(values) {
  emit('onSubmit');
  console.log({
    values,
    isVolunteer: isVolunteer.value,
  });
}

function closeModal() {
  authStore.setLoginPopupOpenStatus(false);
}

function goToRegister() {
  authStore.setLoginPopupOpenStatus(false);
  authStore.setRegisterPopupOpenStatus(true);
}
</script>
