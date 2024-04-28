import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import { AUTH_TOKEN_KEY } from '@/utils/constants';

function isAuthenticated(_to, _from, next) {
  if (localStorage.getItem(AUTH_TOKEN_KEY)) {
    next();
  } else {
    next('/');
  }
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/me',
      name: 'me',
      component: () => import('@/views/ProfileView.vue'),
      beforeEnter: isAuthenticated,
    },
    {
      path: '/profile/:role/:id',
      name: 'profile',
      component: () => import('@/views/PublicProfileView.vue'),
    },
    {
      path: '/findvolunteer',
      name: 'findvolunteer',
      component: () => import('@/views/FindVolunteerView.vue'),
    },
    {
      path: '/requests',
      name: 'requests',
      component: () => import('@/views/RequestsView.vue'),
    },
    {
      path: '/404',
      name: 'not_found',
      component: () => import('@/views/ErrorView.vue'),
      meta: {
        layout: 'EmptyLayout',
      },
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/404',
    },
  ],
});

export default router;
