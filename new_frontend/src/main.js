import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import util from './util'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'
import 'primevue/resources/themes/nova-light/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'
import 'primeflex/primeflex.css'
import ToastService from 'primevue/toastservice';

const backendUrl = 'http://127.0.0.1:8000/api/'

Vue.config.devtools = true;
Vue.config.productionTip = false
Vue.prototype.$axios = axios
axios.defaults.withCredentials = true
Vue.prototype.$url = backendUrl
Vue.prototype.$util = util
Vue.use(ToastService);

router.beforeEach((to, from, next) => {
  console.log(to.name + " <- " + from.name)
  if (store.state.username || to.name === 'Login') {
    if ((to.name === 'Index'|| to.name === 'Login') && store.state.isDoctor) {
      next({name: 'PatientSearch'})
    } else {
      next()
    }
  } else {
    // console.log(store.state)
    axios({
      method: 'get',
      url: backendUrl + 'login/'
    }).then(response => {
      let data = response.data
      if (data.state) {
        store.commit('setUsername', data.data.user.username)
        store.commit('setName', data.data.user.name)
        store.commit('isAdmin', data.data.user.isAdmin)
        store.commit('isDoctor', data.data.user.isDoctor)
        if ((to.name === 'Index'|| to.name === 'Login') && store.state.isDoctor) {
          next({name: 'PatientSearch'})
        } else {
          next()
        }
      } else {
        next({name: 'Login'})
      }
    }), (error) => {
      console.log(error)
    }
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
