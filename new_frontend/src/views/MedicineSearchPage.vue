<template>
  <div>
    <MySideBar :whichActive="'medicineSearch'" class="p-mr-2" />
    <MedicineDataTable :patients="medicines" class="search"/>
  </div>
</template>

<script>
import MedicineDataTable from "../components/dataTables/MedicineDataTable";
import MySideBar from "../components/MySideBar";

export default {
  name: "MedicineSearchPage",
  components: {
    MedicineDataTable,
    MySideBar
  },
  data () {
    return {
      msg: 'Network Error',
      medicines: null,
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