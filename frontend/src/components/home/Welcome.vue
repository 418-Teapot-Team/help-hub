<template>
  <section>
    <div class="bg-section-secondary h-screen flex flex-col">
      <div class="w-full flex justify-center">
        <div class="bg-white h-36 w-[600px] rounded-md mt-10 absolute z-0">
          <div class="bg-primary-light h-36 w-28 absolute rounded-md -mt-3 ml-3 z-10"></div>
          <span class="font-bold text-3xl z-20 absolute text-left h-full mt-4 ml-5"
            >Приєднуйтесь до нашої волонтерської платформи та разом з нами допоможіть змінити світ
            на краще!</span
          >
        </div>
      </div>
      <div class="w-full mt-52 flex justify-around">
        <div class="w-[600px] flex flex-row items-center">
          <div class="ml-6 flex flex-col justify-start gap-2">
            <span class="text-light-text text-xl font-semibold"
              >Допомагайте тим, хто цього потребує, вже сьогодні!</span
            >
            <AppButton text="Розмістити заявку" isBold class="mt-4" />
            <button class="w-fit underline">Стати волонтером</button>
          </div>
          <img class="w-80" src="/images/WelcomeImg.webp" alt="" />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import AppButton from '@/components/atoms/buttons/AppButton.vue';
</script>
