import { defineStore } from 'pinia';
import { ref } from 'vue';
import { httpClient } from '@/utils/HttpClient';
export const useAuthStore = defineStore('auth', () => {
  const isLoginPopupOpen = ref(false);
  const isRegisterPopupOpen = ref(false);

  function setLoginPopupOpenStatus(status) {
    isLoginPopupOpen.value = status;
  }

  function setRegisterPopupOpenStatus(status) {
    isRegisterPopupOpen.value = status;
  }

  async function register(payload) {
    await httpClient.post('', {
      full_name: payload.firstName,
      phone: payload.phone,
      email: payload.email,
      password: payload.password,
      role: payload.role,
    });
  }

  return {
    isLoginPopupOpen,
    isRegisterPopupOpen,
    setLoginPopupOpenStatus,
    setRegisterPopupOpenStatus,
    register,
  };
});
