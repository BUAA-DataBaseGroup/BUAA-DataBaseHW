<template>
  <div>
    <div id="header">
      <div class="inner home-inner">
        <div class="mylogo">
          <router-link v-if="type==='unlogin'" to="/" title="提瓦特招聘">
            <span>提瓦特招聘</span>
          </router-link>
          <router-link v-else to="/homepage_login" title="提瓦特招聘">
            <span>提瓦特招聘</span>
          </router-link>
        </div>
        <div class="nav">
          <ul style="height: 49px">
            <li style="height: 49px" class="">
              <router-link v-if="type==='unlogin'" to="/" style="height: 49px">首页</router-link>
              <router-link v-else to="/homepage_login" style="height: 49px">首页</router-link>
            </li>
            <li style="height: 49px" class="cur"><a style="height: 49px" href="#">职位</a></li>
            <li style="height: 49px" class=""><a style="height: 49px" href="#">校园</a></li>
            <li style="height: 49px" class=""><a style="height: 49px" href="#">公司</a></li>
            <li style="height: 49px" class=""><a style="height: 49px" href="#">咨询</a></li>
            <li style="height: 49px" class=""><a style="height: 49px" href="#">百科</a></li>
          </ul>
        </div>
        <div v-if="type==='unlogin'" class="user-nav">
          <div class="btns">
            <router-link to="/employee_login" rel="nofollow" ka="nlp_resume_upload" class="link-sign-resume" title="上传简历，解析内容，完善注册">我要找工作</router-link>
            <router-link to="/company_login" rel="nofollow" ka="header-geek" class="link-sign-resume" title="上传简历，解析内容，完善注册">我要招聘</router-link>
            <!--            <a href="login.html" ka="header-register" class="btn btn-outline">个人注册登录</a>-->
            <!--            <a href="register.html" ka="header-register" class="btn btn-outline">招聘者注册登录</a>-->
          </div>
        </div>
        <div v-else class="user-nav">
          <ul>
            <li class=""><a ka="header-message" href="#">消息<span class="nav-chat-num"></span></a></li>
            <li v-if="is_employee" class=""><router-link to="/resume">简历</router-link></li>
            <li v-else><router-link :to="'/company/' + get_email">公司信息</router-link></li>
            <li v-if="is_employee" class="nav-dot">·</li>
            <li class="nav-up-file"><router-link v-if="is_employee" to="/resume" class="header-resume-upload" ka="header-resume-upload-2">上传简历</router-link></li>
            <li class="nav-figure" id = "figure" @mouseover="showup()" @mouseleave="disapear()">
              <router-link v-if="is_employee" to="/resume" ka="header-username">
                <span class="label-text" id = "name">{{username}}</span><img src="../images/微信图片_202202151700162.jpg" alt=""/>
              </router-link>
              <router-link v-else :to="'/company/' + get_email" ka="header-username">
                <span class="label-text" id = "name">{{username}}</span><img src="../images/微信图片_202202151700162.jpg" alt=""/>
              </router-link>
              <div class="dropdown" id="droplist">
                <router-link v-if="is_employee" to="/resume" class="personal-center" ka="header-personal">个人中心<span>推荐职位、编辑在线简历</span></router-link>
                <router-link v-else :to="'/company/' + get_email" class="personal-center" ka="header-personal">公司信息中心<span>编辑公司信息、招聘职位</span></router-link>
                <!-- 跟后端对接 -->
                <router-link v-if="is_employee" to="/resume" class="account-set" ka="account_manage">账号与安全中心</router-link>
                <router-link v-else :to="'/company/' + get_email" class="account-set" ka="account_manage">账号与安全中心</router-link>
                <router-link v-if="is_employee" to="/resume" class="privacy-set" ka="privacy_set">通知与隐私设置</router-link>
                <router-link v-else :to="'/company/' + get_email" class="privacy-set" ka="privacy_set">通知与隐私设置</router-link>
                <router-link v-if="is_employee" to="/company_login" class="link-recruit" ka="header-recruit">切换为招聘者</router-link>
                <router-link v-else to="/employee_login" class="link-recruit" ka="header-recruit">切换为找工作者</router-link>
                <router-link to="/" class="link-logout" >退出登录</router-link>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <div style="background: #f4f4f4; height: 100%; width: 100%">
      <head_information :is_check="is_check" />
      <div style="width: 1136px; height: 50px; margin: 30px auto; display: block; background: white; border-radius: 10px">
        <div style="padding-top: 10px; padding-left: 30px">
          <span :class="{covered: is_inf}" style="font-size: 20px; cursor:pointer; margin-right: 30px" @click="to_where(true)">公司简介</span>
          <span :class="{covered: !is_inf}" style="font-size: 20px; cursor:pointer" @click="to_where(false)">招聘职位</span>
        </div>
      </div>

      <div style="width: 1136px; margin: 30px auto; display: block">
        <div style="width: 850px; float: left; margin-right: 15px; margin-bottom: 30px">
          <brief_information :is_check="is_check" v-if="is_inf" style="background: white; border-radius: 10px; padding: 10px 5px 10px 10px;" />
          <positions_information :is_check="is_check" v-else />
        </div>
        <div style="float: left; width: 235px">
          <worktime_and_welfare :is_check="is_check" style="margin-bottom: 30px; background: white; border-radius: 10px" />
          <recruiter_information :is_check="is_check" style="margin-bottom: 30px; background: white; border-radius: 10px" />
        </div>
        <div style="clear:both;"></div>
      </div>
    </div>
  </div>
</template>

<script>
import head_information from "./corporation_information/head_information.vue";
import brief_information from "./corporation_information/brief_information.vue";
import positions_information from "./corporation_information/positions_information.vue";
import worktime_and_welfare from "./corporation_information/worktime_and_welfare.vue";
import recruiter_information from "./corporation_information/recruiter_information.vue";
import global from "./global.js";

export default {
  name: "corporation_information",
  props: ['company_email'],
  data() {
    return {
      username: '1',
      type: 'unlogin',

      is_inf: true
    }
  },
  mounted() {
    if (global.this_type !== 'unlogin') {
      this.get_username()
      this.type = global.this_token
    }

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
      else if (global.this_type === 'company') {
        this.$axios.post('companies/get_corporation_name', {
          email: global.this_email
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then((res) => {
          that.username = res.data.corporation_abbreviation
        })
      }
    },

    to_where(b) {
      this.is_inf = b
    },

    showup(){
      document.getElementById("droplist").style.display = "block";
    },
    disapear(){
      document.getElementById("droplist").style.display = "none";
    }
  },
  components: [
    head_information,
    brief_information,
    positions_information,
    worktime_and_welfare,
    recruiter_information
  ],
  computed: {
    is_employee() {
      return global.this_type==='employee'
    },
    get_email() {
      return global.this_email
    },

    is_check() {
      return global.this_email !== this.company_email
    },
  }
}
</script>

<style scoped>

.covered {
  color: rgb(0, 166, 167);
}

</style>