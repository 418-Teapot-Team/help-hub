<template>
  <Teleport to="#app">
    <div
      class="fixed top-0 left-0 right-0 bottom-0 z-10 bg-black/20 flex justify-center items-center"
      @click="closeModal"
    >
      <vee-form
        :validation-schema="schema"
        @submit="onSubmit"
        class="relative z-20 w-[320px] xs:w-[380px] sm:w-[420px] md:w-[480px] lg:w-[540px] h-fit bg-white shadow-sm px-6 py-6 flex flex-col justify-start items-center gap-y-6 max-h-screen overflow-y-auto"
        @click.stop
      >
        <div @click="closeModal" class="absolute right-4 top-4 cursor-pointer hover:stroke-primary">
          <CloseIcon class="w-6 h-6" />
        </div>
        <h1 class="font-semibold text-2xl">Новий запит</h1>
        <div class="w-full flex flex-col justify-center gap-y-2">
          <AppPlainInput type="text" label="Назва" name="title" />
          <div>
            <span>Місто</span>
            <AppSelectInput v-model="city" label="name" dataKey="id" :options="cities" />
          </div>
          <div>
            <span>Категорія</span>
            <AppSelectInput v-model="category" label="name" dataKey="id" :options="categories" />
          </div>
          <AppTextarea label="Опис" name="description" />
        </div>
        <div class="w-full flex flex-col justify-start items-center gap-y-2">
          <AppButton class="w-full" type="submit" text="Опублікувати" is-bold />
        </div>
      </vee-form>
    </div>
  </Teleport>
</template>
<script setup>
import { onBeforeMount, reactive, ref } from 'vue';
import AppButton from '@/components/atoms/buttons/AppButton.vue';
import AppPlainInput from '@/components/atoms/inputs/AppPlainInput.vue';
import CloseIcon from '@/components/icons/CloseIcon.vue';
import AppTextarea from '../atoms/inputs/AppTextarea.vue';
import AppSelectInput from '../atoms/inputs/AppSelectInput.vue';
import { useRequestsStore } from '@/stores/requests';

const requestsStore = useRequestsStore();

const city = ref(null);
const category = ref(null);

const cities = ref([]);

const categories = ref([]);

onBeforeMount(() => {
  requestsStore.getCategoriesAndCities().then((res) => {
    cities.value = res.cities;
    categories.value = res.categories;
  });
});

const schema = reactive({
  title: 'required|min:3|max:150',
  description: 'max:700',
});

function onSubmit(values) {
  requestsStore
    .createReq({
      ...values,
      city: city.value,
      category: category.value,
    })
    .then(() => {
      requestsStore.setCreateStatus(false);
    });
}

function closeModal() {
  requestsStore.setCreateStatus(false);
}
</script>
