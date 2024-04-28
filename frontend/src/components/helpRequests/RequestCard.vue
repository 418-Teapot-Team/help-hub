<template>
  <div class="bg-white w-full h-fit md:h-56 px-8 py-4 shadow-sm flex flex-col gap-y-2">
    <div class="flex justify-between flex-col md:flex-row gap-y-2">
      <div class="flex flex-col justify-start items-start gap-y-1">
        <span class="text-lg">{{ data?.title }}</span>
        <div class="flex justify-start items-center gap-x-2">
          <div
            class="w-10 h-10 rounded-full overflow-hidden border border-black/20 shadow-sm"
            @click="$router.push(`/profile/requestor/${data?.requestor?.id}`)"
          >
            <img src="/public/images/howWorkImg.webp" />
          </div>
          <div class="flex flex-col">
            <span
              class="text-sm"
              @click="$router.push(`/profile/requestor/${data?.requestor?.id}`)"
              >{{ data?.requestor?.full_name }}</span
            >
            <span class="text-sm text-primary flex justify-start gap-x-1 items-center">
              <LocationIcon class="w-4 h-4" />
              <span>{{ data?.city }}</span>
            </span>
          </div>
        </div>
      </div>
      <div class="flex justify-start gap-x-1">
        <CalendarIcon class="w-5 h-5" />
        <span class="text-sm">{{ data?.created_at }}</span>
      </div>
    </div>
    <p class="text-sm h-36 overflow-y-auto">
      {{ data?.description }}
    </p>
    <div
      class="w-full flex"
      :class="{
        'justify-end': !isMyApply && !isMyRequest,
        'justify-start': isMyApply || isMyRequest,
      }"
    >
      <div class="flex justify-start gap-2 items-center" v-if="isMyApply">
        <div v-if="status === 'denied'" class="flex justify-start gap-2 items-center">
          <DenyIcon class="w-5 h-5" />
          <span>Denied</span>
          <span class="text-sm text-gray-500 self-center pt-0.5">18.06.2024</span>
        </div>
        <div v-if="status === 'pending'" class="flex justify-start gap-x-2 items-center">
          <TImerIcon class="w-5 h-5" />
          <span>Pending</span>
        </div>
        <div v-if="status === 'accepted'" class="flex justify-start gap-x-2 items-center">
          <AcceptIcon class="w-5 h-5" />
          <span>Approved</span>
          <span class="text-sm text-gray-500 self-center pt-0.5">18.06.2024</span>
        </div>
      </div>
      <button
        v-if="isMyRequest"
        @click="viewApplicants"
        class="text-white bg-primary px-4 py-1 shadow-sm hover:bg-simple-gray duration-200"
      >
        View applicants
      </button>
      <button
        v-if="!isMyApply && !isMyRequest && (profileData?.role === 'volunteer' || !profileData)"
        @click="apply"
        class="text-white bg-primary px-4 py-1 shadow-sm hover:bg-simple-gray duration-200"
      >
        Apply
      </button>
    </div>
    <Applicants v-if="isApplicantsShow" @close-modal="isApplicantsShow = false" />
  </div>
</template>
<script setup>
import LocationIcon from '@/components/icons/LocationIcon.vue';
import CalendarIcon from '@/components/icons/CalendarIcon.vue';
import DenyIcon from '@/components/icons/DenyIcon.vue';
import TImerIcon from '@/components/icons/TImerIcon.vue';
import AcceptIcon from '@/components/icons/AcceptIcon.vue';
import Applicants from '@/components/modals/Applicants.vue';
import { ref } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { computed } from 'vue';
import { useRequestsStore } from '@/stores/requests';

const requestsStore = useRequestsStore();
const authStore = useAuthStore();

const isLoggedIn = computed(() => authStore.isLoggedIn);
const profileData = computed(() => authStore.profileData);

const props = defineProps(['isMyApply', 'status', 'isMyRequest', 'data']);

const isApplicantsShow = ref(false);

function viewApplicants() {
  isApplicantsShow.value = true;
}

function apply() {
  if (isLoggedIn.value) {
    requestsStore.apply(props.data.id);
  } else {
    authStore.setLoginPopupOpenStatus(true);
  }
}
</script>
