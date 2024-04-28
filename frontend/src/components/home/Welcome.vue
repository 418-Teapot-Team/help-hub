<template>
  <section>
    <div class="bg-section-secondary h-full flex flex-col w-full">
      <!-- small screen -->
      <div class="w-full h-[calc(100vh-80px)] flex lg:hidden justify-center px-10">
        <div
          class="bg-white mt-12 h-36 w-[calc(100vw-100px)] sm:w-[600px] md:w-[700px] rounded-md absolute z-0"
        >
          <div
            class="bg-primary-light h-36 w-28 absolute md:block rounded-md -mt-3 ml-3 z-10"
          ></div>
          <span
            class="mx-auto font-bold text-md xs:text-xl sm:text-3xl md:text-[31px] z-20 absolute text-left h-full mt-4 md:ml-7 ml-5"
          >
            Приєднюйтесь до нашої волонтерської платформи та разом з нами допоможіть змінити світ на
            краще!</span
          >
        </div>
        <div class="w-full mt-52 flex justify-around lg:hidden">
          <div class="w-[600px] flex flex-col items-center">
            <img class="w-96 lg:hidden" src="/images/WelcomeImg.webp" alt="" />
            <div class="flex flex-col gap-2 mb-12 mt-8 items-center">
              <span class="text-light-text text-xl text-center font-semibold"
                >Допомагайте тим, хто цього потребує, вже сьогодні!</span
              >
              <AppButton text="Розмістити заявку" isBold class="mt-4" />
              <button class="w-fit underline">Стати волонтером</button>
            </div>
          </div>
        </div>
      </div>

      <!-- big screen -->
      <div
        class="hidden h-[calc(100vh-80px)] flex-col lg:flex-row lg:flex xl:justify-evenly md:justify-center items-center xl:px-12 md:px-16 xl:gap-x-10"
      >
        <div class="flex flex-col lg:-mt-20 xl:-mt-0">
          <div class="bg-white xl:h-60 xl:w-[750px] rounded-xl z-0 md:w-[550px] md:h-48">
            <div
              class="bg-primary-light xl:h-64 xl:w-40 md:h-48 md:w-36 absolute md:block rounded-xl xl:-mt-7 md:-mt-3 ml-3 z-10"
            ></div>
            <span
              class="font-semibold text-dark-text xl:text-5xl md:text-3xl xl:w-[700px] md:w-[500px] z-20 absolute text-left mt-5 ml-8"
              >Приєднуйтесь до нашої волонтерської платформи та разом з нами допоможіть змінити світ
              на краще!</span
            >
          </div>
          <div class="w-full xl:mt-20 md:mt-14 flex">
            <div class="w-[600px] flex flex-row items-center">
              <div class="ml-6 flex flex-col justify-start gap-2">
                <span class="text-light-text xl:text-4xl xl:w-96 font-semibold md:text-3xl md:w-80"
                  >Допомагайте тим, хто цього потребує, вже сьогодні!</span
                >
                <div class="flex flex-row gap-x-6 pt-16">
                  <AppButton text="Розмістити заявку" isBold class="xl:py-4 xl:px-5 md:py-3" />
                  <button class="w-fit underline font-semibold text-lg">Стати волонтером</button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- TODO: fix responsivness -->
        <div class="lg:w-[700px] mt-14 lg:-mt-20 xl:-mt-0">
          <img class="xl:w-max md:w-[500px]" src="/images/WelcomeImg.webp" alt="" />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import AppButton from '@/components/atoms/buttons/AppButton.vue';
</script>
