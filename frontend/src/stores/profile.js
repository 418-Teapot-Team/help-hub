import { httpClient } from '@/utils/HttpClient';
import { defineStore } from 'pinia';
import { useToast } from 'vue-toast-notification';
export const useProfileStore = defineStore('profile', () => {
  const $toast = useToast();

  async function getProfie(type, id) {
    try {
      const res = await httpClient.get(`/profile/${type}/${id}`);
      return res.data;
    } catch (e) {
      $toast.error(e.message);
    }
  }

  async function editProfile(payload) {
    try {
      const res = await httpClient.put('/profile/edit', {
        ...payload,
      });
      $toast.success(res.data.message);
    } catch (e) {
      $toast.error(e.message);
    }
  }

  async function getMe() {
    try {
      const res = await httpClient.get('/profile/me');
      return res.data;
    } catch (e) {
      $toast.error(e.message);
    }
  }

  return {
    getProfie,
    editProfile,
    getMe,
  };
});
