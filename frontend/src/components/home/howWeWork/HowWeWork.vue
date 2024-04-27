<template>
  <section>
    <div class="h-[100vh]">
      <div class="flex justify-center mt-32 lg:mt-28 2xl:mt-20">
        <span class="text-dark-text text-4xl md:text-5xl font-semibold">Як ми працюємо?</span>
      </div>
      <div class="flex w-full justify-evenly flex-row xs:items-center py-32 lg:py-32 2xl:py-24">
        <img class="w-[500px] 2xl:w-[700px] hidden lg:block" src="/images/howWorkImg.webp" alt="" />
        <div
          class="border-l-primary xs:w-[410px] 2xl:w-[600px] border-l-[4px] xs:border-l-[6px] md:border-l-8 h-[250px] xs:h-[350px] md:h-[400px] lg:h-[400px] 2xl:h-[500px] flex flex-col justify-between"
        >
          <div
            v-for="(item, idx) in works"
            :key="idx"
            class="flex flex-row items-center gap-x-10 2xl:gap-x-20"
          >
            <div
              class="flex justify-center items-center text-white rounded-full text-xl xs:text-3xl font-semibold bg-primary w-12 h-12 ml-[-26px] xs:w-16 xs:h-16 xs:-ml-9 md:w-[70px] md:h-[70px] md:-ml-[39px] 2xl:w-20 2xl:h-20 2xl:-ml-11"
            >
              {{ idx + 1 }}
            </div>
            <span class="text-xl xs:text-3xl text-dark-text">{{ item.label }}</span>
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
