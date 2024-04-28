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

  async function getMyRequests() {
    try {
      const res = await httpClient.get('/requests/my');
      return res.data;
    } catch (e) {
      $toast.error(e.message);
    }
  }

  async function approve(app_id, req_id) {
    try {
      const res = await httpClient.post('/requests/approve', {
        volunteer_id: app_id,
        request_id: req_id,
      });

      $toast.success(res.data.message);
    } catch (e) {
      $toast.error(e.message);
    }
  }
  return {
    getRequests,
    apply,
    getMyRequests,
    approve,
  };
});
