import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAuthStore = defineStore('auth', () => {
  const isLoginPopupOpen = ref(false);
  const isRegisterPopupOpen = ref(false);

  function setLoginPopupOpenStatus(status) {
    isLoginPopupOpen.value = status;
  }

  function setRegisterPopupOpenStatus(status) {
    isRegisterPopupOpen.value = status;
  }

  return {
    isLoginPopupOpen,
    isRegisterPopupOpen,
    setLoginPopupOpenStatus,
    setRegisterPopupOpenStatus,
  };
});
