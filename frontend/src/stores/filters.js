import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useFiltersStore = defineStore('filters', () => {
  const filters = ref({});

  function addFilter(key, value) {
    if (filters.value[key]) {
      filters.value[key].push(value);
    } else {
      filters.value[key] = [value];
    }
  }

  function removeFilter(key, value) {
    if (!filters.value[key]) {
      return;
    }

    const filterIndex = filters.value[key].findIndex((item) => item === value);
    if (filterIndex > -1) {
      filters.value[key].splice(filterIndex, 1);
    }
  }

  function isActive(key, value) {
    if (!filters.value[key]) {
      return false;
    }
    const filter = filters.value[key].find((item) => item === value);
    return !!filter;
  }

  function clearAllFilters() {
    filters.value = {};
  }

  function parseFromQuery(query) {
    let parsedQuery = {};
    if (query) {
      Object.keys(query).map((key) => {
        parsedQuery[key] = JSON.parse(query[key]);
      });
    }
    filters.value = parsedQuery;
  }

  function getQuerystring() {
    let querystring = '?';
    for (let entry of Object.entries(filters.value)) {
      if (entry[1].length < 1) continue;
      querystring += `${entry[0]}=`;
      querystring += encodeURIComponent(JSON.stringify(entry[1]));
      querystring += '&';
    }

    return querystring.substring(0, querystring.length - 1);
  }

  return {
    filters,
    addFilter,
    removeFilter,
    clearAllFilters,
    isActive,
    parseFromQuery,
    getQuerystring,
  };
});
