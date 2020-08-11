import Vue from 'vue'
import Router from 'vue-router'
import Login from "./views/Login";
import PatientSearchPage from "./views/PatientSearchPage";
import MedicineSearchPage from "./views/MedicineSearchPage"

Vue.use(Router)
// Vue.config.devtools = true;

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/patientSearch',
      name: 'PatientSearch',
      component: PatientSearchPage
    },
    {
      path: '/medicineSearch',
      name: 'MedicineSearch',
      component: MedicineSearchPage
    }
  ]
})
