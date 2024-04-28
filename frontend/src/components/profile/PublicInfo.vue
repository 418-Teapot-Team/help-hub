<template>
  <div
    class="relative w-full lg:max-h-[calc(100vh-144px) h-full border border-black/10 shadow-sm px-8 py-4 flex flex-col justify-start items-center gap-y-4 overflow-auto"
  >
    <div class="w-full flex justify-start items-center">
      <span class="text-xl font-semibold">Інформація</span>
    </div>
    <div class="flex justify-center items-center w-full h-full">
      <div class="w-full flex flex-col justify-between h-full gap-y-6 lg:gap-y-0">
        <div class="flex flex-col gap-y-4 lg:flex-row justify-center items-start gap-x-4 w-full">
          <div class="flex flex-col justify-start items-start gap-y-4 w-full">
            <span class="text-lg underline">Персональні данні</span>
            <div class="flex flex-col justify-center items-start gap-y-1 w-full">
              <span class="font-semibold">Ім'я</span>
              <span class="text-elipsis">{{ publicData?.full_name }}</span>
            </div>
            <div class="flex flex-col justify-center items-start gap-y-1 w-full">
              <span class="font-semibold">Телефон</span>
              <a
                :href="'tel:' + publicData?.phone"
                class="text-elipsis cursor-pointer text-primary"
                >{{ publicData?.phone }}</a
              >
            </div>
            <div class="flex flex-col justify-center items-start gap-y-1 w-full">
              <span class="font-semibold">E-mail</span>
              <a
                :href="'mailto:' + publicData?.email"
                class="text-elipsis cursor-pointer text-primary"
                >{{ publicData?.email }}</a
              >
            </div>
          </div>
          <div class="flex flex-col justify-start items-start gap-y-4 w-full">
            <span class="text-lg underline">Соц. мережі</span>
            <div class="flex flex-col justify-center items-start gap-y-1 w-full">
              <span class="font-semibold">Telegram</span>
              <a
                v-if="publicData?.telegram"
                target="_blank"
                rel="norefferer noopener"
                :href="'https://t.me/' + publicData?.telegram"
                :class="{
                  'text-primary cursor-pointer': publicData?.telegram?.length,
                }"
                >{{ '@' + publicData?.telegram || '-' }}</a
              >
              <span v-else>-</span>
            </div>
            <div class="flex flex-col justify-center items-start gap-y-1 w-full">
              <span class="font-semibold">Facebook</span>
              <a
                v-if="publicData?.facebook"
                target="_blank"
                rel="norefferer noopener"
                :href="'http://www.facebook.com/' + publicData?.facebook"
                :class="{
                  'text-primary cursor-pointer': publicData?.facebook?.length,
                }"
                >{{ '@' + publicData?.facebook || '-' }}</a
              >
              <span v-else>-</span>
            </div>
            <div class="flex flex-col justify-center items-start gap-y-1 w-full">
              <span class="font-semibold">Twitter</span>
              <a
                v-if="publicData?.twitter"
                target="_blank"
                rel="norefferer noopener"
                :href="'https://twitter.com/' + publicData?.twitter"
                :class="{
                  'text-primary cursor-pointer': publicData?.twitter?.length,
                }"
                >{{ '@' + publicData?.twitter || '-' }}</a
              >
              <span v-else>-</span>
            </div>
            <div class="flex flex-col justify-center items-start gap-y-1 w-full">
              <span class="font-semibold">Instagram</span>
              <a
                v-if="publicData?.instagram"
                target="_blank"
                rel="norefferer noopener"
                :href="'http://instagram.com/_u/' + publicData?.instagram"
                :class="{
                  'text-primary cursor-pointer': publicData?.instagram?.length,
                }"
                >{{ '@' + publicData?.instagram || '-' }}</a
              >
              <span v-else>-</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps(['publicData']);
</script>
