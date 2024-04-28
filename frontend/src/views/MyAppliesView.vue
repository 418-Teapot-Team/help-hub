<template>
  <div class="bg-section-secondary w-full h-screenr flex justify-center">
    <div class="flex justify-center h-screen gap-x-4 container">
      <Filters :filters="filtersData" @applyFilters="applyFilters" />
      <RequestList :data="requestsData" lass="overflow-auto pb-10" />
    </div>
  </div>
</template>
<script></script>
