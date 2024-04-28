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
        <h1 class="font-semibold text-2xl">New request</h1>
        <div class="w-full flex flex-col justify-center gap-y-2">
          <AppPlainInput type="text" label="Title" name="title" />
          <div>
            <span>City</span>
            <AppSelectInput v-model="city" label="label" dataKey="id" :options="cities" />
          </div>
          <div>
            <span>Category</span>
            <AppSelectInput
              v-model="category"
              :isMultiple="true"
              :max="3"
              label="label"
              dataKey="id"
              :options="categories"
            />
          </div>
          <AppTextarea label="Description" name="description" />
        </div>
        <div class="w-full flex flex-col justify-start items-center gap-y-2">
          <AppButton class="w-full" type="submit" text="Publish" is-bold />
        </div>
      </vee-form>
    </div>
  </Teleport>
</template>
<script setup>
import { reactive, ref } from 'vue';
import { useAuthStore } from '@/stores/auth';
import AppButton from '@/components/atoms/buttons/AppButton.vue';
import AppPlainInput from '@/components/atoms/inputs/AppPlainInput.vue';
import CloseIcon from '@/components/icons/CloseIcon.vue';
import AppTextarea from '../atoms/inputs/AppTextarea.vue';
import AppSelectInput from '../atoms/inputs/AppSelectInput.vue';

const emit = defineEmits(['onSubmit']);

const authStore = useAuthStore();

const city = ref(null);
const category = ref([]);

const cities = ref([
  {
    label: 'Kyiv',
    id: 'kyiv',
  },
  {
    label: 'Lviv',
    id: 'lviv',
  },
  {
    label: 'Khmelnytskyi',
    id: 'khmelnytskyi',
  },
  {
    label: 'Volodymyr',
    id: 'volodymyr',
  },
  {
    label: 'Vinnytisa',
    id: 'vinnytsia',
  },
]);

const categories = ref([
  {
    label: 'Medicine',
    id: 'meds',
  },
  {
    label: 'Food',
    id: 'food',
  },
  {
    label: 'Military',
    id: 'military',
  },
  {
    label: 'Other',
    id: 'other',
  },
]);

const schema = reactive({
  title: 'required|min:3|max:150',
  description: 'max:700',
});

function onSubmit(values) {
  emit('onSubmit');
  console.log({
    values,
  });
}

function closeModal() {
  authStore.setRegisterPopupOpenStatus(false);
}
</script>
