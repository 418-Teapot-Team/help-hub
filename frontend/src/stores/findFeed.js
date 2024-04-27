import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useFindFeedStore = defineStore('findFeed', () => {
  const volunteers = ref([
    {
      image: '/images/Profile.png',
      name: 'Mykola Balii',
      stat: 5,
      location: 'Хмельницька обл. м. Хмельницький',
      tags: ['водіння', 'програмування'],
      description:
        'Маю велике бажання допомогти у сфері розробки веб застосунків. Готовий також бути водієм та займатися перевезенням гуманітарної допомоги',
    },
    {
      image: '/images/Profile.png',
      name: 'Andrii Balii',
      stat: 5,
      location: 'Хмельницька обл. м. Хмельницький',
      tags: ['водіння', 'програмування'],
      description:
        'Маю велике бажання допомогти у сфері розробки веб застосунків. Готовий також бути водієм та займатися перевезенням гуманітарної допомоги',
    },
    {
      image: '/images/Profile.png',
      name: 'Mykola Balii',
      stat: 5,
      location: 'Хмельницька обл. м. Хмельницький',
      tags: ['водіння', 'програмування'],
      description:
        'Маю велике бажання допомогти у сфері розробки веб застосунків. Готовий також бути водієм та займатися перевезенням гуманітарної допомоги',
    },
    {
      image: '/images/Profile.png',
      name: 'Mykola Balii',
      stat: 5,
      location: 'Хмельницька обл. м. Хмельницький',
      tags: ['водіння', 'програмування'],
      description:
        'Маю велике бажання допомогти у сфері розробки веб застосунків. Готовий також бути водієм та займатися перевезенням гуманітарної допомоги',
    },
    {
      image: '/images/Profile.png',
      name: 'Mykola Balii',
      stat: 5,
      location: 'Хмельницька обл. м. Хмельницький',
      tags: ['водіння', 'програмування'],
      description:
        'Маю велике бажання допомогти у сфері розробки веб застосунків. Готовий також бути водієм та займатися перевезенням гуманітарної допомоги',
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
