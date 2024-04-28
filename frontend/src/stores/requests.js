import { httpClient } from '@/utils/HttpClient';
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { useToast } from 'vue-toast-notification';

export const useRequestsStore = defineStore('requests', () => {
  const $toast = useToast();

  const isCreateOpen = ref(false);

  function setCreateStatus(status) {
    isCreateOpen.value = status;
  }

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

  async function getCategoriesAndCities() {
    try {
      const catRes = await httpClient.get('/categories');
      const citRes = await httpClient.get('/cities');
      return {
        categories: catRes.data,
        cities: citRes.data,
      };
    } catch (e) {
      $toast.error(e.message);
    }
  }

  async function createReq(payload) {
    try {
      const res = await httpClient.post('/requests/create', { ...payload });
      $toast.success(res.data.message);
    } catch (e) {
      $toast.error(e.message);
    }
  }

  async function getMyApplies() {
    try {
      const res = await httpClient.get('/requests/my_applies');
      return res.data;
    } catch (e) {
      $toast.error(e.message);
    }
  }

  async function getVolunteers() {
    try {
      const res = await httpClient.get('/volunteers/all');
      return res.data;
    } catch (e) {
      $toast.error(e.message);
    }
  }

  async function getStats() {
    try {
      const res = await httpClient.get('/stat/general');
      return res.data;
    } catch (e) {
      $toast.error(e.message);
    }
  }
  return {
    isCreateOpen,
    setCreateStatus,
    getRequests,
    apply,
    getMyRequests,
    approve,
    getCategoriesAndCities,
    createReq,
    getMyApplies,
    getVolunteers,
    getStats,
  };
});
