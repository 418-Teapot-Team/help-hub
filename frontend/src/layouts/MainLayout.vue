<template>
  <main>
    <h1>Main!</h1>
    <AppButton :type="buttonType" :text="buttonText" />
    <router-view />
  </main>
</template>

<script>
import AppButton from '../components/atoms/buttons/AppButton.vue';
export default {
  name: 'MainLayout',
  components: {
    AppButton,
  },
  data() {
    return {
      buttonType: 'primary',
      buttonText: 'Реєстрація',
    };
  },
};
</script>
