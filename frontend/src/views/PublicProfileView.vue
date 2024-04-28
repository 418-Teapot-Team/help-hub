<template>
  <section
    id="profile"
    class="px-8 md:px-16 py-8 min-h-[calc(100vh-80px)] md:min-h-0 md:h-[calc(100vh-80px)] h-full overflow-auto"
  >
    <div
      class="flex flex-col items-center md:flex-row justify-center md:items-start h-full gap-x-0 gap-y-8 md:gap-y-0 md:gap-x-8"
    >
      <div class="flex flex-col justify-start gap-y-8 h-full w-full md:w-fit">
        <Avatar :editable="false" :role="route.params.role" />
        <Stats :profileData="profileData" />
      </div>
      <div class="w-full h-full">
        <PublicInfo v-if="profileData" :publicData="profileData" />
      </div>
    </div>
  </section>
</template>
<script setup>
import Avatar from '@/components/profile/Avatar.vue';
import PublicInfo from '@/components/profile/PublicInfo.vue';
import Stats from '@/components/profile/Stats.vue';

import { useProfileStore } from '@/stores/profile';
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const router = useRouter();
const route = useRoute();

const profileStore = useProfileStore();
const profileData = ref({});

onMounted(() => {
  const role = route.params.role;
  const id = route.params.id;
  if (role?.length && id?.length) {
    profileStore.getProfie(role, id).then((res) => {
      profileData.value = res;
      console.log(res);
    });
  } else {
    router.replace('/404');
  }
});
</script>
