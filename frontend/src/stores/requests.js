import { httpClient } from '@/utils/HttpClient';
import { defineStore } from 'pinia';
import { useToast } from 'vue-toast-notification';

export const useRequestsStore = defineStore('requests', () => {
  const $toast = useToast();
  async function getRequests(filters, search) {
    try {
      const res = await httpClient.get('/requests/all', {
        params: {
          ...filters,
          search,
        },
      });
      return res.data;
    } catch (e) {
      $toast.error(e.message);
    }
  }
  async function apply(request_id) {
    try {
      const res = await httpClient.post('/requests/apply', {
        request_id,
      });
      $toast.success(res.data.message);
    } catch (e) {
      $toast.error(e.message);
    }
  }
  return {
    getRequests,
    apply,
  };
});
