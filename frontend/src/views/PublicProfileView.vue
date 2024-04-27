<template>
  <section
    id="profile"
    class="px-8 md:px-16 py-8 min-h-[calc(100vh-80px)] md:min-h-0 md:h-[calc(100vh-80px)] h-full overflow-auto"
  >
    <div
      class="flex flex-col items-center md:flex-row justify-center md:items-start h-full gap-x-0 gap-y-8 md:gap-y-0 md:gap-x-8"
    >
      <div class="flex flex-col justify-start gap-y-8 h-full w-full md:w-fit">
        <Avatar :editable="false" />
        <Stats />
      </div>
      <div class="w-full h-full">
        <PublicInfo />
      </div>
    </div>
  </section>
</template>
<script setup>
import Avatar from '@/components/profile/Avatar.vue';
import PublicInfo from '@/components/profile/PublicInfo.vue';
import Stats from '@/components/profile/Stats.vue';
</script>
