<template>
  <div id="page_background">

    <!-- 导航条开始 -->
    <div id="header">
      <div class="inner home-inner">
        <div class="mylogo">
          <router-link to="/homepage_login" title="提瓦特招聘">
            <span>提瓦特招聘</span>
          </router-link>
        </div>
        <div class="nav">
          <ul>
            <li class=""><router-link to="/homepage_login">首页</router-link><span>&emsp13;&emsp13;&emsp13;&emsp13;&emsp13;</span></li>
            <li class=""><router-link to="/joblist/智能驾驶系统工程师">职位</router-link><span>&emsp13;&emsp13;&emsp13;&emsp13;&emsp13;</span></li>
            <li class=""><a href="#">校园</a><span>&emsp13;&emsp13;&emsp13;&emsp13;&emsp13;</span></li>
            <li class=""><a href="#">公司</a><span>&emsp13;&emsp13;&emsp13;&emsp13;&emsp13;</span></li>
            <li class=""><a href="#">咨询</a><span>&emsp13;&emsp13;&emsp13;&emsp13;&emsp13;</span></li>
            <li class=""><a href="#">百科</a><span>&emsp13;&emsp13;&emsp13;&emsp13;&emsp13;</span></li>
          </ul>
        </div>
        <div class="user-nav">
          <ul>
            <li class=""><a ka="header-message" href="#">消息<span class="nav-chat-num"></span></a></li>
            <li class="cur"><router-link to="/resume">简历</router-link></li>
            <li class="nav-dot">·</li>
            <li class="nav-up-file"><router-link to="/resume" class="header-resume-upload" ka="header-resume-upload-2">上传简历</router-link></li>
            <li class="nav-figure" id = "figure" @mouseover="showup()" @mouseleave="disapear()">
              <router-link to="/resume" ka="header-username">
                <span class="label-text" id = "name">{{username}}</span><img src="../images/微信图片_202202151700162.jpg" alt=""/>
              </router-link>
              <div class="dropdown" id="droplist">
                <router-link to="/resume" class="personal-center" ka="header-personal">个人中心<span>推荐职位、编辑在线简历</span></router-link>
                <!-- 跟后端对接 -->
                <router-link to="/resume" class="account-set" ka="account_manage">账号与安全中心</router-link>
                <router-link to="/resume" class="privacy-set" ka="privacy_set">通知与隐私设置</router-link>
                <router-link v-if="type==='employee'" to="/company_register" class="link-recruit" ka="header-recruit">切换为招聘者</router-link>
                <router-link v-else to="/employee_register" class="link-recruit" ka="header-recruit">我要找工作</router-link>
                <router-link to="/" class="link-logout" >退出登录</router-link>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <!-- 导航条结束 -->

    <div style="padding-top: 20px; margin-left: 10px">
      <resume_catalogue id="resume_catalogue" />
      <resume_main_content id="resume_main_content" />
    </div>
  </div>
</template>

<script>
import resume_catalogue from "./resume/resume_catalogue.vue";
import resume_main_content from "./resume/resume_main_content.vue";
import global from "./global.js";

export default {
  name: "resume",
  data() {
    return {
      username: 'unlogin',
      type: "unlogin"
    }
  },
  mounted: function () {
    this.get_username()
    this.type = global.this_type
  },
  methods: {
    get_username() {
      let that = this
      if (global.this_type === 'employee') {
        this.$axios.post('people/get_my_name', {
          email: global.this_email
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then((res) => {
          that.username = res.data.my_name
        })
      }
    },
    showup(){
      document.getElementById("droplist").style.display = "block";
    },
    disapear(){
      document.getElementById("droplist").style.display = "none";
    }
  },
  components: {
    resume_catalogue,
    resume_main_content
  }
}
</script>

<style scoped>
@import "../assets/css/index_main.css";
@import "../assets/css/tiwate.css";

#page_background {
  height: 100%;
  width: 100%;
  overflow: auto;
  background: #f4f4f4;
}

#resume_catalogue {
  float: left;
  position: fixed;
  margin-left: 100px;
}

#resume_main_content {
  float: left;
  margin: 0 0 20px 300px;
}
</style>