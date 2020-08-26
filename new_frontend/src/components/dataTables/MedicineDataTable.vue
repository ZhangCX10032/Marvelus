<template>
  <div>table<Button class="p-button-danger" icon="pi pi-sign-out" @click="req()"/></div>

</template>

<script>
  import Button from 'primevue/button';
  export default {
    name: "MedicineDataTable",
    components: {
      Button
    },
    props: {
      medicines: Array,
      isDoctor: Boolean
    },
    methods: {
      // req: function() {
      //   let command = "accept 20200602104449884166\naccept 20200602104449639165"
      //   this.$axios.post('https://26c4c43dk5.execute-api.ap-southeast-1.amazonaws.com/default/acceptDeclineOrder',
      //       {
      //         driverNumber: "+6593556445", // for authentication
      //         commandCount: "2",
      //         command: command
      //     });
      // }
    }
  }
</script>

<style scoped>

</style>