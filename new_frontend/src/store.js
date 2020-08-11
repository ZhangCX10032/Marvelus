import Vue from 'vue'
import Vuex from 'vuex'

Vue.config.devtools = true;
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    username: null,
    name: null,
    isAdmin: false,
    isDoctor: false
  },
  mutations: {
    setUsername (state, username) {
      state.username = username
    },
    setName (state, name) {
      state.name = name
    },
    isAdmin (state, isAdmin) {
      state.isAdmin = isAdmin
    },
    isDoctor (state, isDoctor) {
      state.isDoctor = isDoctor
    }
  },
  actions: {

  }
})
