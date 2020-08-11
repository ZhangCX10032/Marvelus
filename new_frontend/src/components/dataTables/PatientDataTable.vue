<template>
  <div>
    <DataTable :value="patients" sortMode="multiple" class="p-datatable-patients" :paginator="true" :rows="10"
               dataKey="id" :rowHover="true" :filters="filters"
               paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
               :rowsPerPageOptions="[10,25,50]" currentPageReportTemplate="正在显示从第{first}项到第{last}项/共{totalRecords}项">
      <template #header>
        <div class="table-header">
            患者列表
            <span class="p-input-icon-left">
                <i class="pi pi-search" />
                <InputText v-model="filters['global']" placeholder="全局搜索：姓名/性别/电话..." />
            </span>
        </div>
      </template>
      <template #empty>
        没有符合条件的患者。
      </template>
      <Column field="patient_id" header="编号" :sortable="true">
        <template #body="slotProps">
          <span class="p-column-title"></span>
          {{slotProps.data.patient_id}}
        </template>
        <template #filter>
          <InputText type="text" v-model="filters['patient_id']" class="p-column-filter" placeholder="搜索编号"/>
        </template>
      </Column>
      <Column field="name" header="姓名" :sortable="true" filterMatchMode="contains">
        <template #body="slotProps">
            <span class="p-column-title">姓名</span>
            {{slotProps.data.name}}
        </template>
        <template #filter>
          <InputText type="text" v-model="filters['name']" class="p-column-filter" placeholder="搜索名字"/>
        </template>
      </Column>
      <Column field="gender" header="性别" :sortable="true" filterMatchMode="equals">
        <template #body="slotProps">
          <span class="p-column-title">Status</span>
          <span>{{slotProps.data.gender}}</span>
        </template>
        <template #filter>
          <Dropdown v-model="filters['gender']" :options="genders" placeholder="选择性别" class="p-column-filter" :showClear="true">
            <template #option="slotProps">
              <span>{{slotProps.option}}</span>
            </template>
          </Dropdown>
        </template>
      </Column>
      <Column field="birthdate" header="生日" :sortable="true" filterMatchMode="custom" :filterFunction="filterDate">
        <template #body="slotProps">
          <span class="p-column-title">Date</span>
          {{slotProps.data.birthdate}}
        </template>
        <template #filter>
          <Calendar v-model="filters['birthdate']" dateFormat="yy-mm-dd" :monthNavigator="true"
                    :showButtonBar="true" :locale="cn" :yearNavigator="true"
                    class="p-column-filter" placeholder="生日" yearRange="1900:2050"/>
        </template>
      </Column>
      <Column field="phone_number" header="手机" filterMatchMode="contains">
        <template #body="slotProps">
            <span class="p-column-title">手机</span>
            {{slotProps.data.phone_number}}
        </template>
        <template #filter>
          <InputText type="text" v-model="filters['phone_number']" class="p-column-filter" placeholder="搜索手机"/>
        </template>
      </Column>
      <Column>
        <template #body>
          <Button label="就诊"></Button>
        </template>
      </Column>
    </DataTable>
  </div>
</template>

<script>
import Button from 'primevue/button';
import Calendar from 'primevue/calendar';
import Column from 'primevue/column';
import DataTable from 'primevue/datatable';
import Dropdown from 'primevue/dropdown'
import InputText from 'primevue/inputtext';
export default {
  name: 'PatientDataTable',
  components: {
    Button,
    Calendar,
    Column,
    DataTable,
    Dropdown,
    InputText
  },
  props: {
    patients: Array,
    isDoctor: Boolean
  },
  data(){
    return {
      filters:{},
      genders: [
          '男', '女'
      ],
      cn: {
                firstDayOfWeek: 0,
                dayNames: ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"],
                dayNamesShort: ["周日", "周一", "周二", "周三", "周四", "周五", "周六"],
                dayNamesMin: ["日","一","二","三","四","五","六"],
                monthNames: [ "一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月" ],
                monthNamesShort: [ "一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月" ],
                today: '今天',
                clear: '清空',
                dateFormat: 'mm/dd/yy',
                weekHeader: 'Wk'
            }
    }
  },
  methods: {
    filterDate(value, filter) {
      if (filter === undefined || filter === null || (typeof filter === 'string' && filter.trim() === '')) {
        return true;
      }

      if (value === undefined || value === null) {
        return false;
      }

      return value === this.formatDate(filter);
    },
    formatDate(date) {
      let month = date.getMonth() + 1;
      let day = date.getDate();

      if (month < 10) {
        month = '0' + month;
      }

      if (day < 10) {
        day = '0' + day;
      }

      return date.getFullYear() + '-' + month + '-' + day;
    }
  }
}
</script>

<style lang="scss" scoped>
  /deep/ .p-paginator {
    .p-paginator-current {
      margin-left: auto;
    }
  }

  /deep/ .p-progressbar {
    height: .5rem;
    background-color: #D8DADC;

    .p-progressbar-value {
      background-color: #00ACAD;
    }
  }

  .table-header {
    display: flex;
    justify-content: space-between;
  }

  /deep/ .p-datepicker {
    min-width: 25rem;

    td {
      font-weight: 400;
    }
  }

  /deep/ .p-datatable.p-datatable-patients {
    .p-datatable-header {
      padding: 1rem;
      text-align: left;
      font-size: 1.5rem;
    }

    .p-paginator {
      padding: 1rem;
    }

    .p-datatable-thead > tr > th {
      text-align: left;
    }

    .p-datatable-tbody > tr > td {
      cursor: auto;
    }

    .p-dropdown-label:not(.p-placeholder) {
      text-transform: uppercase;
    }
  }

  /* Responsive */
  .p-datatable-patients .p-datatable-tbody > tr > td .p-column-title {
    display: none;
  }

  @media screen and (max-width: 64em) {
    /deep/ .p-datatable {
      &.p-datatable-patients {
        .p-datatable-thead > tr > th,
        .p-datatable-tfoot > tr > td {
          display: none !important;
        }

        .p-datatable-tbody > tr > td {
          text-align: left;
          display: block;
          border: 0 none !important;
          width: 100% !important;
          float: left;
          clear: left;
          border: 0 none;

          .p-column-title {
            padding: .4rem;
            min-width: 30%;
            display: inline-block;
            margin: -.4rem 1rem -.4rem -.4rem;
            font-weight: bold;
          }
        }
      }
    }
  }
</style>
