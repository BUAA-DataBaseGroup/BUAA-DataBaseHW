<template>
  <div>
    <div id = "wrap">
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
      <div id="main">
        <div class="job-banner">
          <div class="inner home-inner">
            <div class="job-primary detail-box">
              <div class="info-primary">
                <div class="job-status">
                  <span>招聘中</span>
                </div>
                <div class="name">
                  <h1 title="算法实习生">{{ position_name }}</h1>
                  <span class="salary">{{ position_salary }}</span>
                </div>
                <p> <span class="text-desc text-experiece">{{ position_address }} {{position_education}} {{position_experience}}</span>
                  <span class="text-desc text-degree">本科</span></p>
                <div class="tag-container-new">
                  <div class="tag-more" style="opacity: 1;">
                    <span class="link-more">...</span>
                    <div class="tag-all job-tags">
                      <span>五险一金</span><span>补充医疗保险</span><span>定期体检</span><span>年终奖</span><span>带薪年假</span>
                    </div>
                  </div>
                </div>
                <div class="job-tags">
                  <span>五险一金</span><span>补充医疗保险</span><span>定期体检</span><span>年终奖</span><span>带薪年假</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="smallbanner">
          <div class="inner home-inner">
            <div class="company-info">
              <div class="name">

                <span class="job-title">算法实习生</span>
                <span class="badge">130-250元/天</span>
              </div>
            </div>
            <div class="tag-container-new">
              <div class="tag-more" style="opacity: 1;">
                <span class="link-more">...</span>
                <div class="tag-all job-tags">
                  <span>五险一金</span><span>补充医疗保险</span><span>定期体检</span><span>年终奖</span><span>带薪年假</span>
                </div>
              </div>
              <div class="job-tags">
                <span>五险一金</span><span>补充医疗保险</span><span>定期体检</span><span>年终奖</span><span>带薪年假</span>
              </div>
            </div>
          </div>
        </div>
        <div class="job-box">
          <div class="inner home-inner">
<!--            <div class="job-sider">-->
<!--              <div class="sider-company">-->
<!--                <p class="title">公司基本信息</p>-->
<!--                <div class="company-info">-->
<!--                  <a ka="job-detail-company-logo_custompage" title="oppo北京" target="_blank">-->
<!--                    <img src="https://img.bosszhipin.com/beijin/upload/com/logo/20190723/dec13c5d7ec747d28760a7e72aa2accde863c4ee8c44fd202406bb64591ff6a3.png?x-oss-process=image/resize,w_120,limit_0" alt=""/>-->
<!--                  </a>-->
<!--                  <a ka="job-detail-company_custompage"  title="oppo北京" target="_blank">-->
<!--                    oppo北京-->
<!--                  </a>-->
<!--                </div>-->
<!--                <p><i class="icon-stage"></i>不需要融资</p>-->
<!--                <p><i class="icon-scale"></i>1000-9999人</p>-->
<!--                <p><i class="icon-industry"></i><a ka="job-detail-brandindustry" href="/i100020/">互联网</a></p>-->
<!--                <a class="look-all" ka="more-similar-jobs1">查看全部职位</a>-->
<!--              </div>-->
<!--              <div class="similar-job-wrapper">-->
<!--                <h3>相似职位<a href="/c101010100-p100120/e_109/" rel="nofollow" ka="more-similar-jobs2" target="_blank">更多相似职位</a></h3>-->
<!--                <ul class="similar-job-list">-->
<!--                  <li>-->
<!--                    <a ka="job_sug_1" target="_blank">-->
<!--                      <div class="similar-job-info">-->
<!--                        <span class="similar-job-name">算法实习生</span>-->
<!--                        <span class="similar-job-salary">200-300元/天</span>-->
<!--                      </div>-->
<!--                      <p class="similar-job-attr">-->
<!--                                            <span class="similar-job-company" data-url="/gongsir/ab8eb97d47e715431nx53dm9FVE~.html" ka="job_sug_brandjob1_custompage">-->
<!--                                                <span class="job-company-logo" data-url="/gongsi/ab8eb97d47e715431nx53dm9FVE~.html" ka="job_sug_brand1_custompage">-->
<!--                                                    <img src="https://img.bosszhipin.com/beijin/upload/com/workfeel/20220530/7bf6f160950405e992d8ff5e7c6b58e3fad5fbaae9043a380540a8a26a61b674636473dacc1237fd.jpg?x-oss-process=image/resize,w_100,limit_0" alt="">-->
<!--                                                </span>-->
<!--                                                <span class="company-name">牵手</span>-->
<!--                                            </span>-->
<!--                        <span class="similar-job-location">北京</span>-->
<!--                      </p>-->
<!--                    </a>-->
<!--                  </li>-->
<!--                  <li>-->
<!--                    <a ka="job_sug_2" target="_blank">-->
<!--                      <div class="similar-job-info">-->
<!--                        <span class="similar-job-name">算法工程师(实习)</span>-->
<!--                        <span class="similar-job-salary">300-400元/天</span>-->
<!--                      </div>-->
<!--                      <p class="similar-job-attr">-->
<!--                                                <span class="similar-job-company" data-url="/gongsir/f9a5b0b441e187631nJ_2dy8FVs~.html" ka="job_sug_brandjob2_custompage">-->
<!--                                                    <span class="job-company-logo" data-url="/gongsi/f9a5b0b441e187631nJ_2dy8FVs~.html" ka="job_sug_brand2_custompage">-->
<!--                                                        <img src="https://img.bosszhipin.com/beijin/mcs/banner/03e20c586edcc2a1f2b9ec79de83368acfcd208495d565ef66e7dff9f98764da.png?x-oss-process=image/resize,w_100,limit_0" alt="">-->
<!--                                                    </span>-->
<!--                                                    <span class="company-name">京东科技集团</span>-->
<!--                                                </span>-->
<!--                        <span class="similar-job-location">北京</span>-->
<!--                      </p>-->
<!--                    </a>-->
<!--                  </li>-->
<!--                  <li>-->
<!--                    <a ka="job_sug_3" target="_blank">-->
<!--                      <div class="similar-job-info">-->
<!--                        <span class="similar-job-name">算法工程师(实习)</span>-->
<!--                        <span class="similar-job-salary">300-400元/天</span>-->
<!--                      </div>-->
<!--                      <p class="similar-job-attr">-->
<!--                                                <span class="similar-job-company" data-url="/gongsir/0810a0f85e31859b33Zy2tU~.html" ka="job_sug_brandjob3_custompage">-->
<!--                                                    <span class="job-company-logo" data-url="/gongsi/0810a0f85e31859b33Zy2tU~.html" ka="job_sug_brand3_custompage">-->
<!--                                                        <img src="https://img.bosszhipin.com/beijin/upload/com/logo/20191018/87d69d0f0d2c61d0e9b8789f4b9527609af890db898d4bda24f0b08151e58387.jpg?x-oss-process=image/resize,w_100,limit_0" alt="">-->
<!--                                                    </span>-->
<!--                                                    <span class="company-name">微软中国</span>-->
<!--                                                </span>-->
<!--                        <span class="similar-job-location">北京</span>-->
<!--                      </p>-->
<!--                    </a>-->
<!--                  </li>-->
<!--                  <li>-->
<!--                    <a ka="job_sug_4" target="_blank">-->
<!--                      <div class="similar-job-info">-->
<!--                        <span class="similar-job-name">搜索算法实习生</span>-->
<!--                        <span class="similar-job-salary">230-300元/天</span>-->
<!--                      </div>-->
<!--                      <p class="similar-job-attr">-->
<!--                                                <span class="similar-job-company" data-url="/gongsir/980f48937a13792b1nd63d0~.html" ka="job_sug_brandjob4_custompage">-->
<!--                                                    <span class="job-company-logo" data-url="/gongsi/980f48937a13792b1nd63d0~.html" ka="job_sug_brand4_custompage">-->
<!--                                                        <img src="https://img.bosszhipin.com/beijin/mcs/chatphoto/20190408/c23f08b24983fffa26a3a8ba19a463523cc05a6873981b80bf124ddd6c45f629_s.jpg?x-oss-process=image/resize,w_100,limit_0" alt="">-->
<!--                                                    </span>-->
<!--                                                    <span class="company-name">滴滴出行</span>-->
<!--                                                </span>-->
<!--                        <span class="similar-job-location">北京</span>-->
<!--                      </p>-->
<!--                    </a>-->
<!--                  </li>-->
<!--                  <li>-->
<!--                    <a ka="job_sug_5" target="_blank">-->
<!--                      <div class="similar-job-info">-->
<!--                        <span class="similar-job-name">图像算法实习生</span>-->
<!--                        <span class="similar-job-salary">280-380元/天</span>-->
<!--                      </div>-->
<!--                      <p class="similar-job-attr">-->
<!--                                                <span class="similar-job-company" data-url="/gongsir/efa878c051261c7433Z6.html" ka="job_sug_brandjob5_custompage">-->
<!--                                                    <span class="job-company-logo" data-url="/gongsi/efa878c051261c7433Z6.html" ka="job_sug_brand5_custompage">-->
<!--                                                        <img src="https://img.bosszhipin.com/beijin/mcs/banner/55e497a3c749352df771d48a6ed5d279cfcd208495d565ef66e7dff9f98764da.jpg?x-oss-process=image/resize,w_100,limit_0" alt="">-->
<!--                                                    </span>-->
<!--                                                    <span class="company-name">好未来</span>-->
<!--                                                </span>-->
<!--                        <span class="similar-job-location">北京</span>-->
<!--                      </p>-->
<!--                    </a>-->
<!--                  </li>-->
<!--                </ul>-->
<!--                <a class="look-all" rel="nofollow" target="_blank" ka="more-similar-jobs3">查看全部职位</a>-->
<!--              </div>-->
<!--              <div class="promotion-img"><a href="/salaryxc/" target="_blank" ka="query_pay_click"><img src="https://img.bosszhipin.com/static/file/2022/ne3elze9ld1653961014120.jpg" alt="" /></a></div>-->
<!--            </div>-->
            <div class="job-detail">
              <div class="job-detail-section">
                <div class="job-sec-text">
                  {{position_description}}
                </div>
                <div class="job-boss-info">
                  <div class="detail-figure">
                    <img src="https://img.bosszhipin.com/boss/avatar/avatar_16.png?x-oss-process=image/resize,w_100,limit_0" alt="" />
                  </div>
                  <!-- 联系人 -->
                  <h2 class="name">{{ position_re_name }}<i class="icon-vip"></i>

                  </h2>
                  <div class="boss-info-attr">
                    <span class="boss-active-time">{{ position_re_post }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import global from "./global.js";
import { CodeToText } from 'element-china-area-data'

export default {
  name: "job",
  props: ['job_id', 'email', 're_id'],
  data() {
    return {
      type: 'unlogin',
      username: '1',

      position_name: "",
      position_address: "",
      position_experience: "",
      position_education: "",
      position_salary: "",
      position_description: "",

      position_re_name: "",
      position_re_post: ""
    }
  },
  computed: {
    islogin() {
      return global.this_type
    },
    is_employee() {
      return global.this_type==='employee'
    },
    get_email() {
      return global.this_email
    }
  },
  mounted() {
    if (global.this_type !== 'unlogin') {
      this.get_username()
      this.type = global.this_token
    }
    this.init_job()
  },
  methods: {
    init_job() {
      let that = this
      this.$axios.post('companies/get_job', {
        email: this.email,
        id: this.job_id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        console.log(res.data)
        that.position_name = res.data.position_name
        that.position_address = this.getProvince(res.data.position_address[0])
        that.position_experience = this.experience(res.data.position_experience)
        that.position_education = this.education(res.data.position_education)
        that.position_salary = res.data.position_salary_from + "-" + res.data.position_salary_to + "千"
        that.position_description = res.data.position_description

        that.$axios.post('companies/get_recruiter', {
          email: this.email,
          id: this.re_id
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then((res) => {
          console.log(res.data)
          that.position_re_name = res.data.recruiter_name
          that.position_re_post = res.data.recruiter_post
        })
      })
    },
    getProvince(province_code) {
      return CodeToText[province_code]
    },
    experience(s) {
      switch (s) {
        case 0:
          return "在校生"
        case 1:
          return "应届生"
        case 2:
          return "一年以内"
        case 3:
          return "1-3年"
        case 4:
          return "3-5年"
        case 5:
          return "5-10年"
        case 6:
          return "10年以上"
        default:
          return "error"
      }
    },
    education(s) {
      switch (s) {
        case 0:
          return "初中及以下"
        case 1:
          return "中专/中技"
        case 2:
          return "高中"
        case 3:
          return "大专"
        case 4:
          return "本科"
        case 5:
          return "硕士"
        case 6:
          return "博士"
        default:
          return "error"
      }
    },
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
    showup() {
      document.getElementById("droplist").style.display = "block";
    },
    disapear() {
      document.getElementById("droplist").style.display = "none";
    }
  },
}
</script>

<style scoped>
@import "../assets/css/tiwate.css";
@import "../assets/css/jobs.css";
</style>