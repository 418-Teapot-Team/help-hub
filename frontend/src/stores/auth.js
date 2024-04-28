import { defineStore } from 'pinia';
import { ref } from 'vue';
import { httpClient } from '@/utils/HttpClient';
import { useToast } from 'vue-toast-notification';
import { AUTH_TOKEN_KEY } from '@/utils/constants';

export const useAuthStore = defineStore('auth', () => {
  const $toast = useToast();

  const isLoginPopupOpen = ref(false);
  const isRegisterPopupOpen = ref(false);
  const profileData = ref(null);
  const isLoggedIn = ref(false);

  function setLoginPopupOpenStatus(status) {
    isLoginPopupOpen.value = status;
  }

  function setRegisterPopupOpenStatus(status) {
    isRegisterPopupOpen.value = status;
  }

  async function signUp(payload) {
    try {
      const res = await httpClient.post('/auth/signup', {
        ...payload,
      });
      $toast.success(res.data.message);
      setRegisterPopupOpenStatus(false);
      setLoginPopupOpenStatus(true);
    } catch (e) {
      $toast.error(e.message);
    }
  }

  async function signIn(payload) {
    try {
      const res = await httpClient.post('/auth/signin', {
        ...payload,
      });
      localStorage.setItem(AUTH_TOKEN_KEY, res.data.access_token);
      $toast.success(res.data.message);
      setLoginPopupOpenStatus(false);
      isLoggedIn.value = true;
    } catch (e) {
      $toast.error(e.message);
      isLoggedIn.value = false;
    }
  }

  async function whoAmI() {
    try {
      const res = await httpClient.get('/auth/whoami');
      profileData.value = res.data;
      isLoggedIn.value = true;
    } catch (e) {
      $toast.error(e.message);
      isLoggedIn.value = false;
    }
  }

  function signOut() {
    localStorage.removeItem(AUTH_TOKEN_KEY);
    isLoggedIn.value = false;
    profileData.value = null;
  }

  return {
    isLoginPopupOpen,
    isRegisterPopupOpen,
    profileData,
    isLoggedIn,
    setLoginPopupOpenStatus,
    setRegisterPopupOpenStatus,
    signUp,
    signIn,
    whoAmI,
    signOut,
  };
});
