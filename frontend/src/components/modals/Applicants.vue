<template>
  <div
    class="bg-black/20 z-10 fixed top-0 left-0 right-0 bottom-0 flex justify-center items-center"
    @click="closeModal"
  >
    <div
      class="w-[320px] sm:w-[380px] md:w-[460px] lg:w-[620px] text-center shadow-sm bg-gray-100 border border-black/20 px-16 pt-16 pb-8 relative flex flex-col justify-center items-center gap-y-8"
      @click.stop
    >
      <div @click="closeModal" class="absolute right-4 top-4 cursor-pointer hover:stroke-primary">
        <CloseIcon class="w-8 h-8" />
      </div>
      <span>Applicants</span>
      <div
        class="flex flex-col justify-start gap-y-4 items-start max-h-[380px] overflow-auto w-full"
      >
        <div
          class="px-4 py-2 lg:py-1 border border-black/20 shadow-sm flex flex-col lg:flex-row justify-between w-full h-fit lg:h-16 gap-y-4"
        >
          <div class="flex flex-col lg:flex-row justify-start items-center gap-2">
            <div class="rounded-full h-10 w-10 overflow-hidden border border-black/20">
              <img src="/public/images/howWorkImg.webp" />
            </div>
            <div class="flex flex-col justify-center items-center lg:items-start gap-y-0.5">
              <span class="text-sm font-semibold">John Doe</span>
              <span class="text-xs text-gray-500">+38(067)-777-77-77</span>
            </div>
          </div>
          <div class="flex justify-center items-center gap-x-3">
            <button class="text-white bg-red-500 px-4 h-8 shadow-sm hover:bg-red-600 duration-200">
              Deny
            </button>
            <button
              class="text-white bg-green-500 px-4 h-8 shadow-sm hover:bg-green-600 duration-200"
            >
              Confirm
            </button>
          </div>
        </div>
        <div
          class="px-4 py-2 lg:py-1 border border-black/20 shadow-sm flex flex-col lg:flex-row justify-between w-full h-fit lg:h-16 gap-y-4"
        >
          <div class="flex flex-col lg:flex-row justify-start items-center gap-2">
            <div class="rounded-full h-10 w-10 overflow-hidden border border-black/20">
              <img src="/public/images/howWorkImg.webp" />
            </div>
            <div class="flex flex-col justify-center items-center lg:items-start gap-y-0.5">
              <span class="text-sm font-semibold">John Doe</span>
              <span class="text-xs text-gray-500">+38(067)-777-77-77</span>
            </div>
          </div>
          <div class="flex justify-center items-center gap-x-3">
            <button class="text-white bg-red-500 px-4 h-8 shadow-sm hover:bg-red-600 duration-200">
              Deny
            </button>
            <button
              class="text-white bg-green-500 px-4 h-8 shadow-sm hover:bg-green-600 duration-200"
            >
              Confirm
            </button>
          </div>
        </div>
        <div
          class="px-4 py-2 lg:py-1 border border-black/20 shadow-sm flex flex-col lg:flex-row justify-between w-full h-fit lg:h-16 gap-y-4"
        >
          <div class="flex flex-col lg:flex-row justify-start items-center gap-2">
            <div class="rounded-full h-10 w-10 overflow-hidden border border-black/20">
              <img src="/public/images/howWorkImg.webp" />
            </div>
            <div class="flex flex-col justify-center items-center lg:items-start gap-y-0.5">
              <span class="text-sm font-semibold">John Doe</span>
              <span class="text-xs text-gray-500">+38(067)-777-77-77</span>
            </div>
          </div>
          <div class="flex justify-center items-center gap-x-3">
            <button class="text-white bg-red-500 px-4 h-8 shadow-sm hover:bg-red-600 duration-200">
              Deny
            </button>
            <button
              class="text-white bg-green-500 px-4 h-8 shadow-sm hover:bg-green-600 duration-200"
            >
              Confirm
            </button>
          </div>
        </div>
        <div
          class="px-4 py-2 lg:py-1 border border-black/20 shadow-sm flex flex-col lg:flex-row justify-between w-full h-fit lg:h-16 gap-y-4"
        >
          <div class="flex flex-col lg:flex-row justify-start items-center gap-2">
            <div class="rounded-full h-10 w-10 overflow-hidden border border-black/20">
              <img src="/public/images/howWorkImg.webp" />
            </div>
            <div class="flex flex-col justify-center items-center lg:items-start gap-y-0.5">
              <span class="text-sm font-semibold">John Doe</span>
              <span class="text-xs text-gray-500">+38(067)-777-77-77</span>
            </div>
          </div>
          <div class="flex justify-center items-center gap-x-3">
            <button class="text-white bg-red-500 px-4 h-8 shadow-sm hover:bg-red-600 duration-200">
              Deny
            </button>
            <button
              class="text-white bg-green-500 px-4 h-8 shadow-sm hover:bg-green-600 duration-200"
            >
              Confirm
            </button>
          </div>
        </div>
        <div
          class="px-4 py-2 lg:py-1 border border-black/20 shadow-sm flex flex-col lg:flex-row justify-between w-full h-fit lg:h-16 gap-y-4"
        >
          <div class="flex flex-col lg:flex-row justify-start items-center gap-2">
            <div class="rounded-full h-10 w-10 overflow-hidden border border-black/20">
              <img src="/public/images/howWorkImg.webp" />
            </div>
            <div class="flex flex-col justify-center items-center lg:items-start gap-y-0.5">
              <span class="text-sm font-semibold">John Doe</span>
              <span class="text-xs text-gray-500">+38(067)-777-77-77</span>
            </div>
          </div>
          <div class="flex justify-center items-center gap-x-3">
            <button class="text-white bg-red-500 px-4 h-8 shadow-sm hover:bg-red-600 duration-200">
              Deny
            </button>
            <button
              class="text-white bg-green-500 px-4 h-8 shadow-sm hover:bg-green-600 duration-200"
            >
              Confirm
            </button>
          </div>
        </div>
        <div
          class="px-4 py-2 lg:py-1 border border-black/20 shadow-sm flex flex-col lg:flex-row justify-between w-full h-fit lg:h-16 gap-y-4"
        >
          <div class="flex flex-col lg:flex-row justify-start items-center gap-2">
            <div class="rounded-full h-10 w-10 overflow-hidden border border-black/20">
              <img src="/public/images/howWorkImg.webp" />
            </div>
            <div class="flex flex-col justify-center items-center lg:items-start gap-y-0.5">
              <span class="text-sm font-semibold">John Doe</span>
              <span class="text-xs text-gray-500">+38(067)-777-77-77</span>
            </div>
          </div>
          <div class="flex justify-center items-center gap-x-3">
            <button class="text-white bg-red-500 px-4 h-8 shadow-sm hover:bg-red-600 duration-200">
              Deny
            </button>
            <button
              class="text-white bg-green-500 px-4 h-8 shadow-sm hover:bg-green-600 duration-200"
            >
              Confirm
            </button>
          </div>
        </div>
        <div
          class="px-4 py-2 lg:py-1 border border-black/20 shadow-sm flex flex-col lg:flex-row justify-between w-full h-fit lg:h-16 gap-y-4"
        >
          <div class="flex flex-col lg:flex-row justify-start items-center gap-2">
            <div class="rounded-full h-10 w-10 overflow-hidden border border-black/20">
              <img src="/public/images/howWorkImg.webp" />
            </div>
            <div class="flex flex-col justify-center items-center lg:items-start gap-y-0.5">
              <span class="text-sm font-semibold">John Doe</span>
              <span class="text-xs text-gray-500">+38(067)-777-77-77</span>
            </div>
          </div>
          <div class="flex justify-center items-center gap-x-3">
            <button class="text-white bg-red-500 px-4 h-8 shadow-sm hover:bg-red-600 duration-200">
              Deny
            </button>
            <button
              class="text-white bg-green-500 px-4 h-8 shadow-sm hover:bg-green-600 duration-200"
            >
              Confirm
            </button>
          </div>
        </div>
        <div
          class="px-4 py-2 lg:py-1 border border-black/20 shadow-sm flex flex-col lg:flex-row justify-between w-full h-fit lg:h-16 gap-y-4"
        >
          <div class="flex flex-col lg:flex-row justify-start items-center gap-2">
            <div class="rounded-full h-10 w-10 overflow-hidden border border-black/20">
              <img src="/public/images/howWorkImg.webp" />
            </div>
            <div class="flex flex-col justify-center items-center lg:items-start gap-y-0.5">
              <span class="text-sm font-semibold">John Doe</span>
              <span class="text-xs text-gray-500">+38(067)-777-77-77</span>
            </div>
          </div>
          <div class="flex justify-center items-center gap-x-3">
            <button class="text-white bg-red-500 px-4 h-8 shadow-sm hover:bg-red-600 duration-200">
              Deny
            </button>
            <button
              class="text-white bg-green-500 px-4 h-8 shadow-sm hover:bg-green-600 duration-200"
            >
              Confirm
            </button>
          </div>
        </div>
        <div
          class="px-4 py-2 lg:py-1 border border-black/20 shadow-sm flex flex-col lg:flex-row justify-between w-full h-fit lg:h-16 gap-y-4"
        >
          <div class="flex flex-col lg:flex-row justify-start items-center gap-2">
            <div class="rounded-full h-10 w-10 overflow-hidden border border-black/20">
              <img src="/public/images/howWorkImg.webp" />
            </div>
            <div class="flex flex-col justify-center items-center lg:items-start gap-y-0.5">
              <span class="text-sm font-semibold">John Doe</span>
              <span class="text-xs text-gray-500">+38(067)-777-77-77</span>
            </div>
          </div>
          <div class="flex justify-center items-center gap-x-3">
            <button class="text-white bg-red-500 px-4 h-8 shadow-sm hover:bg-red-600 duration-200">
              Deny
            </button>
            <button
              class="text-white bg-green-500 px-4 h-8 shadow-sm hover:bg-green-600 duration-200"
            >
              Confirm
            </button>
          </div>
        </div>
        <div
          class="px-4 py-2 lg:py-1 border border-black/20 shadow-sm flex flex-col lg:flex-row justify-between w-full h-fit lg:h-16 gap-y-4"
        >
          <div class="flex flex-col lg:flex-row justify-start items-center gap-2">
            <div class="rounded-full h-10 w-10 overflow-hidden border border-black/20">
              <img src="/public/images/howWorkImg.webp" />
            </div>
            <div class="flex flex-col justify-center items-center lg:items-start gap-y-0.5">
              <span class="text-sm font-semibold">John Doe</span>
              <span class="text-xs text-gray-500">+38(067)-777-77-77</span>
            </div>
          </div>
          <div class="flex justify-center items-center gap-x-3">
            <button class="text-white bg-red-500 px-4 h-8 shadow-sm hover:bg-red-600 duration-200">
              Deny
            </button>
            <button
              class="text-white bg-green-500 px-4 h-8 shadow-sm hover:bg-green-600 duration-200"
            >
              Confirm
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import CloseIcon from '@/components/icons/CloseIcon.vue';

const emit = defineEmits(['closeModal']);

function closeModal() {
  emit('closeModal');
}
</script>
