import Vue from 'vue'
import VueRouter from 'vue-router'

// route components
import ContactsList from '../components/ContactsLit.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/contacts',
    component: ContactsList,
  }
]

export default new VueRouter({
  routes,
})
