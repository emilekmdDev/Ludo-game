import { createRouter, createWebHistory } from 'vue-router'

import Table_jcj from '../views/Table_jcj.vue'
import Table_jcb from '@/views/Table_jcb.vue'
import Room_config from '@/views/Room_config.vue'
import Table_jcj_multi_room from '@/views/Table_jcj_multi_room.vue'

import Error from '../views/Error.vue' 
import Home from '@/views/Home.vue'
import Login from '@/components/Login.vue'
import Logout from '@/components/Logout.vue'
import Sign_in from '@/components/Sign_in.vue'

const routes = [

  {
    path:'/home',
    name:'home',
    component:Home,
  },

  {
    path:'/jcj',
    name:'Table_jcj',
    component: Table_jcj,
    props:true,
    meta: { requiresAuth: true },
  },

  {
    path:'/jcb', 
    name:'Table_jcb',
    component:Table_jcb,
    meta: { requiresAuth: true },
  },

  {
    path:'/room_config',
    name:'room_config',
    component:Room_config,
    meta: { requiresAuth: true },
  },

  {
    path:'/jcjonline/:room_name',
    name:'table_jcj_multi_room',
    component:Table_jcj_multi_room,
    meta:{ requiresAuth:true }
  },

  
  {
    path:'/login',
    name:'login',
    component:Login,
  },

  {
    path:'/logout',
    name:'logout',
    component:Logout,
  },

  {
    path:'/sign-in',
    name:'sign-in',
    component:Sign_in,
    meta: { noRequiresAuth: true },
  },
  
  // {
  //   path:'/jcj-online',
  //   name:'Table_jcb-online',
  //   component:Table_jcb-online
  // },

  {
    path: '/:pathMatch(.*)*', 
    name: 'NotFound', 
    component: Error 
  },

  {
    path:'/not-found',
    name:'404_page',
    component:Error
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('user');  // Vérifie si l'utilisateur est connecté

  // Si la route nécessite une authentification et que l'utilisateur n'est pas connecté
  if (to.matched.some(record => record.meta.requiresAuth) && !isAuthenticated) {
    next({ name: 'login' });  // Rediriger vers la page de connexion
  } else {
    next();  // Continuer vers la route
  }
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('user');  // Vérifie si l'utilisateur est connecté

  // Si la route nécessite une authentification et que l'utilisateur est pas connecté
  if (to.matched.some(record => record.meta.noRequiresAuth) && isAuthenticated) {
    next({ name: 'home' });  // Rediriger vers la page de connexion
  } else {
    next();  // Continuer vers la route
  }
});


export default router
