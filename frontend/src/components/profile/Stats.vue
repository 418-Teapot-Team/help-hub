<template>
  <div
    class="relative w-full md:w-[240px] h-full border border-black/10 shadow-sm px-8 py-4 flex flex-col justify-start items-start md:items-center gap-y-4"
  >
    <span class="text-xl font-semibold">Статистика</span>
    <div>
      <ul class="flex flex-col justify-start items-start gap-y-3">
        <li class="flex flex-col justify-center gap-y-1" v-if="profileData?.closed_requests">
          <span class="text-base">Closed requests:</span>
          <span class="text-primary font-semibold">{{ profileData?.closed_requests }}</span>
        </li>
        <li class="flex flex-col justify-center gap-y-1">
          <span class="text-base">Using platform since:</span>
          <span class="text-primary font-semibold">{{ profileData?.created_at }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
defineProps(['profileData']);
</script>
