<template>
  <div>
    <Button icon="pi pi-arrow-right" @click="visibleLeft = !visibleLeft"  class="p-mr-2"/>
    <SideBar :visible.sync="visibleLeft" :baseZIndex="1000">
      <h3>Left Sidebar</h3>
    </SideBar>
    <SideBar :whichActive="'patientSearch'" />
<!--    <div class="search">-->
<!--      <div class="searchbar">-->
<!--        <span class="my-keyword">患者姓名:</span>-->
<!--        <input type="text" placeholder="姓名" v-model="keyword" class="my-input" @keyup.enter="searchPatients(keyword)"/>-->
<!--        <Button label="搜索" @click="getPatients(keyword)"></Button>-->
<!--      </div>-->
    <BasicPatientDataTable :patients="patients"/>
<!--    </div>-->
  </div>
</template>

<script>
// import SideBar from "../components/SideBar";
import SideBar from "primevue/sidebar";
import Button from 'primevue/button';
import BasicPatientDataTable from "../components/lists/BasicPatientDataTable";

export default {
  name: "PatientSearchPage",
  components: {
    BasicPatientDataTable,
    SideBar,
    Button
  },
  data () {
    return {
      msg: 'Network Error',
      patients: null,
      visibleLeft: false,
      state: false,
      keyword: ''
    }
  },
  mounted () {
    this.getPatients(null)
  },
  methods: {
    getPatients: function (keyword) {
      this.$axios.request({
        url: keyword ? this.$url + 'patients/search/' + keyword + '/' : this.$url + 'patients/all/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.patients = data.data.patients
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    }
  }
}
</script>

<style scoped>
  .search{
    padding-left: 30px;
    padding-right: 30px;
    width: 100%;
    height: 100%;

    width: calc(100% - 175px);
    float:right;
  }
  .p-mr-2{
    float: contour;
  }
</style>