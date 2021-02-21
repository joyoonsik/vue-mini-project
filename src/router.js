import Vue from 'vue'
import VueRouter from 'vue-router'

import Rhome from './views/Rhome'
import Home from './views/Home'
import About from './views/About'

Vue.use(VueRouter)

const router = new VueRouter({
    mode: "history",
    routes: [
        // config
        {
            path: '/',
            component: Rhome
        },
        {
            path: '/Home',
            component: Home
        },
        {
            path: '/about',
            component: About
        }
    ]
});

export default router;