import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useFindFeedStore = defineStore('findFeed', () => {
  const volunteers = ref([
    {
      image: '/images/Profile.png',
      name: 'Mykola Balii',
      location: 'Хмельницька обл. м. Хмельницький',
    },
    {
      image: '/images/Profile.png',
      name: 'Mykola Balii',
      location: 'Хмельницька обл. м. Хмельницький',
    },
    {
      image: '/images/Profile.png',
      name: 'Mykola Balii',
      location: 'Хмельницька обл. м. Хмельницький',
    },
    {
      image: '/images/Profile.png',
      name: 'Mykola Balii',
      location: 'Хмельницька обл. м. Хмельницький',
    },
    {
      image: '/images/Profile.png',
      name: 'Mykola Balii',
      location: 'Хмельницька обл. м. Хмельницький',
    },
    {
      image: '/images/Profile.png',
      name: 'Mykola Balii',
      location: 'Хмельницька обл. м. Хмельницький',
    },
    {
      image: '/images/Profile.png',
      name: 'Mykola Balii',
      location: 'Хмельницька обл. м. Хмельницький',
    },
    {
      image: '/images/Profile.png',
      name: 'Mykola Balii',
      location: 'Хмельницька обл. м. Хмельницький',
    },
    {
      image: '/images/Profile.png',
      name: 'Mykola Balii',
      location: 'Хмельницька обл. м. Хмельницький',
    },
    {
      image: '/images/Profile.png',
      name: 'Mykola Balii',
      location: 'Хмельницька обл. м. Хмельницький',
    },
    {
      image: '/images/Profile.png',
      name: 'Mykola Balii',
      location: 'Хмельницька обл. м. Хмельницький',
    },
    {
      image: '/images/Profile.png',
      name: 'Mykola Balii',
      location: 'Хмельницька обл. м. Хмельницький',
    },
  ]);

  async function fetchVolunteerData() {
    //TODO: actually fetch the data
    console.log('fetched!');
  }

  return {
    volunteers,
    fetchVolunteerData,
  };
});
