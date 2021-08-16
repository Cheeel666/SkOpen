import Vue from 'vue';
import Router from 'vue-router';
import Courorts from '@/components/Courorts';
import CourortRosa from '@/components/CourortRosa';
import CourortLaura from '@/components/CourortLaura';
import CourortGorod from '@/components/CourortGorod';
import Login from '@/components/Login';
import Register from '@/components/Registration';
import Home from '@/components/Home';
import Profile from '@/components/Profile';
import Admin from '@/components/Admin';

Vue.use(Router);

/* eslint-disable */

const router = new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: { guest: true },
    },
    {
      path: '/register',
      name: 'Register',
      component: Register,
      meta: { guest: true },
    },
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/resorts',
      name: 'Courorts',
      component: Courorts,
      meta: { requiresAuth: true },
    },
    {
      path: '/resorts/Rosa',
      name: 'CourortRosa',
      component: CourortRosa,
      meta: { requiresAuth: true },
    },
    {
      path: '/resorts/Laura',
      name: 'CourortLaura',
      component: CourortLaura,
      meta: { requiresAuth: true },
    },
    {
      path: '/resorts/Polyana',
      name: 'CourortGorod',
      component: CourortGorod,
      meta: { requiresAuth: true },
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile,
      meta: { requiresAuth: true },
    },
    {
      path: '/admin',
      name: 'Admin',
      component: Admin,
      meta: { requiresAuth: true, is_admin: true },
    },
  ],
  mode: 'history',
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (localStorage.getItem('jwt') === null) {
      next({
        name: 'Login',
      });
    } else {
      if (to.matched.some(record => record.meta.is_admin)) {
        if (localStorage.getItem('role') === 'user') {
          next({
            name: 'Profile',
          });
        } else {
          next();
        }
      } else {
        next();
      }
    }
  } else if (to.matched.some(record => record.meta.guest)) {
    if (localStorage.getItem('jwt') != null) {
      next({
        name: 'Profile',
      });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
