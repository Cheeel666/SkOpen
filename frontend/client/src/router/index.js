import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Courorts from '@/components/Courorts';
import CourortRosa from '@/components/CourortRosa';
import CourortLaura from '@/components/CourortLaura';
import CourortGorod from '@/components/CourortGorod';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/resorts',
      name: 'Courorts',
      component: Courorts,
    },
    {
      path: '/resorts/rosakhutor',
      name: 'CourortRosa',
      component: CourortRosa,
    },
    {
      path: '/resorts/laura',
      name: 'CourortLaura',
      component: CourortLaura,
    },
    {
      path: '/resorts/gorod',
      name: 'CourortGorod',
      component: CourortGorod,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
  mode: 'history',
});
