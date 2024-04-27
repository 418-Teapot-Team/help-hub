<template>
  <section>
    <div class="h-[100vh]">
      <div class="flex justify-center mt-20">
        <span class="text-dark-text text-4xl font-semibold">Як ми працюємо?</span>
      </div>
      <div class="flex w-full justify-center flex-row gap-x-36 xs:items-center py-24">
        <img class="w-[600px] hidden lg:block" src="/images/howWorkImg.webp" alt="" />
        <div
          class="border-l-primary border-l-4 xs:border-l-8 h-[250px] xs:h-[500px] flex flex-col justify-between"
        >
          <div v-for="(item, idx) in works" :key="idx" class="flex flex-row items-center gap-x-8">
            <div
              class="flex justify-center items-center text-white rounded-full text-2xl font-semibold bg-primary w-12 h-12 ml-[-26px] xs:w-20 xs:h-20 xs:-ml-11"
            >
              {{ idx + 1 }}
            </div>
            <span class="text-2xl text-dark-text">{{ item.label }}</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const works = ref([
  { label: 'Tak i pracuemo' },
  { label: 'Pracuemo azh pilyka letit' },
  { label: 'Tak tezh pracuemo' },
  { label: 'Jak tilki ne pracuemo...' },
]);
</script>
