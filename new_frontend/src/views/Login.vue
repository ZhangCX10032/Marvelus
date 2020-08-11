<template>
  <div>
    <div class="login-wrap">
      <h3>诊所登录</h3>
      <p v-show="showHelp">{{ help }}</p>
      <input type="text" placeholder="请输入用户名" v-model="username">
      <input type="password" placeholder="请输入密码" v-model="password" @keyup.enter="login">
      <button v-on:click="login">登录</button>
    </div>
  </div>
</template>

<script>
// import store from "../store";

export default {
  name: 'Login',
  data () {
    return {
      showHelp: false,
      help: '',
      username: '',
      password: ''
    }
  },
  mounted () {
    if (this.$store.state.username) {
      this.$router.push({name: 'home'})
    }
  },
  methods: {
    login () {
      this.$axios({
        method: 'post',
        url: this.$url + 'login/',
        data: {
          'username': this.username,
          'password': this.$util.encrypt(this.password)
        },
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        transformRequest: [
          function (data) {
            let ret = ''
            for (let it in data) {
              ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
            }
            return ret
          }
        ]
      }).then(response => {
        if (response.data.state) {
          // console.log(this.$store.state)
          console.log(this)
          // console.log(response.data)
          this.$store.commit('setUsername', response.data.data.user.username)
          this.$store.commit('setName', response.data.data.user.name)
          this.$store.commit('isAdmin', response.data.data.user.isAdmin)
          this.$store.commit('isDoctor', response.data.data.user.isDoctor)
          // if(this.$store){
          //   console.log(this.$store)
          // } else {
          //   console.log("store false")
          // }
          if (this.$store.state.isDoctor){
            this.$router.push({name: 'PatientSearch'})
          } else {
            this.$router.push({name: 'Login'})
          }
        } else {
          this.help = response.data.error
          this.showHelp = true
        }
      }), (error) => {
        console.log(error)
      }
    }
  }
}
</script>

<style scoped>
h3 {
  margin-top: 200px;
}
.login-wrap {
  text-align:center;
}
input {
  display:block;
  width:250px;
  height:40px;
  line-height:40px;
  margin:0 auto;
  margin-top: 20px;
  margin-bottom: 20px;
  outline:none;
  border:1px solid #888;
  padding:10px;
  box-sizing:border-box;
}
p {
  color:red;
}
button {
  display:block;
  width:250px;
  height:40px;
  line-height: 40px;
  margin:0 auto;
  border:none;
  background-color:#1565c0;
  color:#fff;
  font-size:16px;
  margin-bottom:5px;
}
</style>
