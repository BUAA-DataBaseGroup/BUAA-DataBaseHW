<template>
  <div class="container" style="left: 50%; margin-left: -180px">
    <!-- 登录 -->
    <div class="form-box login-box">
      <div class="form">
        <h2 class="title">个人登录</h2>
        <input v-model="input_email" type="email" placeholder="请输入电子邮箱" class="input">
        <input v-model="input_password" type="password" placeholder="请输入密码" class="input">
        <!--          <a class="link">忘记密码?</a>-->
        <div style="height: 50px"></div>
        <button class="btn" @click="check_login_status">登录</button>
        <router-link to="/employee_register" class="link">注册</router-link>
      </div>
    </div>
  </div>
</template>


<script>
import global from "../global.js";

export default {
  name: "employee_login",
  data() {
    return {
      input_email: "20373398@buaa.edu.cn",
      input_password: "123qweasd"
    }
  },
  methods: {
    email_blur() {
      let verify = /^\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}/;
      return !verify.test(this.input_email);
    },
    check_login_status() {
      let that = this

      if (this.email_blur()) {
        this.$message("请输入正确的邮箱格式")
      }
      else if (this.input_password.length === 0) {
        this.$message("请输入密码")
      }
      else {
        this.$axios({
          method: 'post',
          url: '/users/login',
          data: {
            email: this.input_email,
            password: this.input_password,
            is_company: false
          }
        }).then(function (res) {
          let status = res.data.status_code
          if (status === 0) {
            global.this_type = 'employee'
            global.this_email = res.data.email
            global.this_token = res.data.token
            that.$message('恭喜您成功登录')
            that.$router.push({
              path: "/homepage_login"
            })
          }
          else if (status === 1) {
            that.$message('未查询到此用户！')
          }
          else if (status === 2) {
            that.$message("密码错误，请再次尝试！")
          }
          else {
            that.$message("用户类型错误！")
          }
        }).catch(function (error) {
          console.log(error)
        })
      }
    }
  }
}
</script>

<style scoped>
html{
  font-size: 16px;
  width: 100%;
  height: 100%;
}
body{
  background: url(../../images/注册背景图.jfif.crdownload) no-repeat center;
  background-size: cover;
  /*display: grid;*/
  /*display: 100%;*/
  overflow: hidden;
  place-items: center;
  align-items: center;
}
.title{
  font-weight: 300;
  margin: 0 0 1.25rem;
}
.link{
  color: #333;
  font-size: 0.9rem;
  margin: 1.5rem 0;
  text-decoration: none;
  cursor: pointer;
}
.container{
  background: #fff;
  border-radius: 0.7rem;
  box-shadow: 0 9px 17px rgba(0, 0, 0, 0.25),0 7px 7px rgba(0,0,0,0.22);
  width: 360px;
  height: 600px;
  position: relative;
  overflow: hidden;
  top: 50px;
}
/* 隐藏登录模块 */
.form-box{
  width:100%;
  height: 100%;
  position: absolute;
  top:0;
  left:0;
  transition: all 0.6s ease-in-out;
}
.btn{
  background: #07c160;
  border: none;
  color: #fff;
  cursor: pointer;
  font-size: 1.0rem;
  padding: 0.6rem 3rem;
  font-weight: bold;
  margin-top: 1.5rem;
  border-radius: 0.2rem;
  transition: transform 80ms ease-in;
}
.btn:active{
  transform:scale(0.9);
}
.form{
  width: 100%;
  height: 100%;
  background: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 3rem;
  box-sizing: border-box;
}
input{
  border: none;
  background: #f5f5f5;
  margin: 0.5rem 0;
  padding: 0.9rem;
  width: 100%;
}

</style>