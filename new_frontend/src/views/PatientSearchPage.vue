<template>
  <div>
    <MySideBar :whichActive="'patientSearch'" class="p-mr-2" />
    <PatientDataTable :patients="patients" class="search"/>
  </div>
</template>

<script>
import MySideBar from "../components/MySideBar";
import PatientDataTable from "../components/dataTables/PatientDataTable";

export default {
  name: "PatientSearchPage",
  components: {
    PatientDataTable,
    MySideBar,
  },
  data () {
    return {
      msg: 'Network Error',
      patients: null,
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

    width: calc(100% - 135px);
    float:right;
  }
  .p-mr-2{
    width: 125px;
    float: contour;
  }
</style>