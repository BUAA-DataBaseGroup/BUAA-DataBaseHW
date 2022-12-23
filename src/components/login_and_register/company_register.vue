<template>
  <div  class="container" style="left: 50%; margin-left: -180px">
    <div class="form-box register-box">
      <div class="form">
        <h2 class="title">招聘者注册</h2>
        <input v-model="input_corporation_name" type="text" placeholder="请输入公司全称" class="input">
        <input v-model="input_corporation_abbreviation" type="text" placeholder="请输入公司简称" class="input">
        <input v-model="input_email" type="email" placeholder="请输入电子邮箱" class="input">
        <input v-model="input_password1" type="password" placeholder="请输入密码" class="input" title="密码不能为纯数字或字母，密码长度需要大于8小于18">
        <input v-model="input_password2" type="password" placeholder="请再次输入密码" class="input" title="密码不能为纯数字或字母，密码长度需要大于8小于18">
        <button class=" btn" @click="register">注册</button>
        <router-link to="company_login" id="loginBut" class="link">登录</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "company_register",
  data() {
    return {
      input_corporation_name: "北京航空航天大学",
      input_corporation_abbreviation: "北航",
      input_email: "user_xk@163.com",
      input_password1: "123qweasd",
      input_password2: "123qweasd"
    }
  },
  methods: {
    email_blur() {
      let verify = /^\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}/;
      return !verify.test(this.input_email);
    },
    register() {
      let that = this

      if (this.input_corporation_name.length === 0) {
        this.$message("请输入贵公司全称")
      }
      else if (this.input_corporation_abbreviation.length === 0) {
        this.$message("请输入贵公司简称")
      }
      else if (this.email_blur()) {
        this.$message("请输入正确的邮箱格式")
      }
      else if (this.input_password1.length === 0) {
        this.$message("请输入密码")
      }
      else if (this.input_password2.length === 0) {
        this.$message("请再次输入密码")
      }
      else {
        this.$axios({
          method: 'post',
          url: '/users/register',
          data: {
            email: this.input_email,
            corporation_name: this.input_corporation_name,
            corporation_abbreviation: this.input_corporation_abbreviation,
            password1: this.input_password1,
            password2: this.input_password2,
            is_company: true,
          }
        }).then(function (res) {
          let register_status = res.data.status_code
          console.log(res.data)
          if (register_status === 0) {
            that.$message('恭喜您注册成功')
            that.$router.push({
              path: "/company_login"
            })
          }
          else if (register_status === 3) {
            that.$message('两次输入密码不一致！')
          }
          else if (register_status === 1) {
            that.$message('该邮箱已被注册！')
          }
          else if (register_status === 2) {
            that.$message('密码不符合规范！')
          }
          else {
            that.$message("异常错误！")
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