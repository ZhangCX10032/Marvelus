<template>
    <div class="sidebar-menu sidebar-h">
        <div class="sidebar sidebar-inverse">
          <ul class="nav sidebar-nav sidebar-left">
            <li class="tab" :class="{ active: whichActive === 'patientSearch' }" @click="goPatientsSearch()"><a>患者信息</a></li>
            <li class="tab" :class="{ active: whichActive === 'medicineSearch' }" @click="goPatientsSearch()"><a>药方查询</a></li>
          </ul>
        </div>
    </div>
</template>

<script>

export default {
    name: 'SideBar',
    props: {
        whichActive: String
    },
    data() {
        return {}
    },
    methods: {
        goPatientsSearch: function () {
            if (this.$route.name != 'PatientSearch') {
                this.$router.push({name: 'PatientSearch'})
            }
        }
    }
}
</script>

<style scoped>
.sidebar-menu {
  display: inline-block;
  float: left;
}
.tab{
  border-radius: 10px;
}
.tab:hover {
  cursor: pointer;
}
.sidebar-h{
  background-color: #1976d2;
}
.sidebar-left{
  font-size: 18px;
  font-weight: bold;
  background: #1e88e5;
}
.sidebar-inverse {
  border: #1565c0;
  background-color:#1565c0;

}
.sidebar-inverse .sidebar-nav > .active > a,
.sidebar-inverse .sidebar-nav > .active > a:hover,
.sidebar-inverse .sidebar-nav > .active > a:focus {
  color: #1976d2;
  background-color: white;
}
.sidebar-inverse .sidebar-nav > li > a {
  color: white;
}
.sidebar-inverse .nsidebar-nav > li > a:hover {
  color: lightblue;
}
</style>