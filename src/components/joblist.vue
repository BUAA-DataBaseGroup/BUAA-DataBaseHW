<template>
  <div id = "wrap" class="page-job has-header has-footer">
<!--    <script src="../JavaScript/index_js.js"></script>-->
    <!-- 导航条开始 -->
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
    <!-- 导航条结束 -->
    <!-- 搜索条结束 -->
    <div class="page-job-wrapper" style= "padding-top:0;" >
      <!--  -->
      <div class="job-search-wrapper">
        <div class="job-search-box clearfix">
          <div class="job-search-form">
            <span ka="switch_city_dialog_open" class="city-label">北京</span>
            <div class="search-input-box"><div class="input-wrap input-wrap-text">
              <!---->
              <!---->
              <input v-model="search" autocomplete="on" spellcheck="false" type="text" placeholder="搜索职位、公司" class="input">
              <!----><!----><!----><!---->
            </div>
              <!---->
            </div>
            <router-link :to="get_link_joblist(search)" ka="job_search_btn_click" class="search-btn">搜索</router-link>
          </div>
        </div>
        <div class="search-condition-wrapper clearfix">
          <div class="city-area-select expand">
            <div class="city-area-current">
              <i class="ui-icon-location">

              </i>
              <span class="area-current-text">北京</span>
              <!---->
            </div>
            <div class="city-area-dropdown">
              <div class="area-dropdown-item">
                <span class="label">城市</span>
                <ul class="dropdown-city-list">
                  <li ka="sel-city-100010000" class="">全国</li>
                  <li ka="sel-city-101010100" class="active">北京</li>
                  <li ka="sel-city-101020100" class="">上海</li>
                  <li ka="sel-city-101280100" class="">广州</li>
                  <li ka="sel-city-101280600" class="">深圳</li>
                  <li ka="sel-city-101210100" class="">杭州</li>
                  <li ka="sel-city-101030100" class="">天津</li>
                  <li ka="sel-city-101110100" class="">西安</li>
                  <li ka="sel-city-101190400" class="">苏州</li>
                  <li ka="sel-city-101200100" class="">武汉</li>
                  <li ka="sel-city-101230200" class="">厦门</li>
                  <li ka="sel-city-101250100" class="">长沙</li>
                  <li ka="sel-city-101270100" class="">成都</li>
                  <li ka="sel-city-101180100" class="">郑州</li>
                  <li ka="sel-city-101040100" class="">重庆</li>
                  <li>其它城市</li>
                </ul>
              </div>
              <div class="area-dropdown-item">
                <span class="label">区域</span>
                <div class="area-select-wrapper">
                  <div class="area-select-container">
                    <ul class="dropdown-area-list">
                      <li v-for="item in beijing_" ><router-link :to="get_link_joblist('北京'+item)">{{item}}</router-link></li>
                    </ul>
                  </div>
                  <div class="area-select-container clearfix">
                    <a href="javascript:" class="expand-btn">展开全部</a>
                    <ul class="dropdown-area-list">
                      <li>不限</li>
                      <li ka="sel-area-0" class="">安定门</li>
                      <li ka="sel-area-1" class="">安华</li>
                      <li ka="sel-area-2" class="">奥林匹克公园</li>
                      <li ka="sel-area-3" class="">奥运村</li>
                      <li ka="sel-area-4" class="">安贞</li>
                      <li ka="sel-area-5" class="">北辰</li>
                      <li ka="sel-area-6" class="">北工大</li>
                      <li ka="sel-area-7" class="">八里桥</li>
                      <li ka="sel-area-8" class="">八里庄</li>
                      <li ka="sel-area-9" class="">北沙滩</li>
                      <li ka="sel-area-10" class="">百子湾</li>
                      <li ka="sel-area-11" class="">CBD</li>
                      <li ka="sel-area-12" class="">草房</li>
                      <li ka="sel-area-13" class="">传媒大学</li>
                      <li ka="sel-area-14" class="">朝青</li>
                      <li ka="sel-area-15" class="">成寿寺</li>
                      <li ka="sel-area-16" class="">朝外</li>
                      <li ka="sel-area-17" class="">常营</li>
                      <li ka="sel-area-18" class="">朝阳大悦城</li>
                      <li ka="sel-area-19" class="">朝阳公园</li>
                      <li ka="sel-area-20" class="">朝阳门</li>
                      <li ka="sel-area-21" class="">慈云寺</li>
                      <li ka="sel-area-22" class="">东坝</li>
                      <li ka="sel-area-23" class="">东大桥</li>
                      <li ka="sel-area-24" class="">定福庄</li>
                      <li ka="sel-area-25" class="">豆各庄</li>
                      <li ka="sel-area-26" class="">大郊亭</li>
                      <li ka="sel-area-27" class="">大山子</li>
                      <li ka="sel-area-28" class="">大屯</li>
                      <li ka="sel-area-29" class="">对外经贸</li>
                      <li ka="sel-area-30" class="">大望路</li>
                      <li ka="sel-area-31" class="">东小口</li>
                      <li ka="sel-area-32" class="">东直门</li>
                      <li ka="sel-area-33" class="">二外</li>
                      <li ka="sel-area-34" class="">垡头</li>
                      <li ka="sel-area-35" class="">高碑店</li>
                      <li ka="sel-area-36" class="">甘露园</li>
                      <li ka="sel-area-37" class="">国贸</li>
                      <li ka="sel-area-38" class="">广渠门</li>
                      <li ka="sel-area-39" class="">工体</li>
                      <li ka="sel-area-40" class="">国展</li>
                      <li ka="sel-area-41" class="">管庄</li>
                      <li ka="sel-area-42" class="">花家地</li>
                      <li ka="sel-area-43" class="">呼家楼</li>
                      <li ka="sel-area-44" class="">欢乐谷</li>
                      <li ka="sel-area-45" class="">红庙</li>
                      <li ka="sel-area-46" class="">和平街</li>
                      <li ka="sel-area-47" class="">和平里</li>
                      <li ka="sel-area-48" class="">华威桥</li>
                      <li ka="sel-area-49" class="">惠新</li>
                      <li ka="sel-area-50" class="">惠新西街</li>
                      <li ka="sel-area-51" class="">旧宫</li>
                      <li ka="sel-area-52" class="">建国门</li>
                      <li ka="sel-area-53" class="">建国门内</li>
                      <li ka="sel-area-54" class="">劲松</li>
                      <li ka="sel-area-55" class="">将台路</li>
                      <li ka="sel-area-56" class="">建外</li>
                      <li ka="sel-area-57" class="">酒仙桥</li>
                      <li ka="sel-area-58" class="">健翔桥</li>
                      <li ka="sel-area-59" class="">林萃</li>
                      <li ka="sel-area-60" class="">柳芳</li>
                      <li ka="sel-area-61" class="">来广营</li>
                      <li ka="sel-area-62" class="">亮马桥</li>
                      <li ka="sel-area-63" class="">蓝色港湾</li>
                      <li ka="sel-area-64" class="">立水桥</li>
                      <li ka="sel-area-65" class="">马甸</li>
                      <li ka="sel-area-66" class="">牡丹园</li>
                      <li ka="sel-area-67" class="">马泉营</li>
                      <li ka="sel-area-68" class="">麦子店</li>
                      <li ka="sel-area-69" class="">鸟巢</li>
                      <li ka="sel-area-70" class="">南磨房</li>
                      <li ka="sel-area-71" class="">南苑</li>
                      <li ka="sel-area-72" class="">农业展览馆</li>
                      <li ka="sel-area-73" class="">潘家园</li>
                      <li ka="sel-area-74" class="">青年路</li>
                      <li ka="sel-area-75" class="">仁和</li>
                      <li ka="sel-area-76" class="">十八里店</li>
                      <li ka="sel-area-77" class="">首都机场</li>
                      <li ka="sel-area-78" class="">石佛营</li>
                      <li ka="sel-area-79" class="">四惠</li>
                      <li ka="sel-area-80" class="">孙河</li>
                      <li ka="sel-area-81" class="">四惠东</li>
                      <li ka="sel-area-82" class="">双井</li>
                      <li ka="sel-area-83" class="">水立方</li>
                      <li ka="sel-area-84" class="">十里河</li>
                      <li ka="sel-area-85" class="">十里堡</li>
                      <li ka="sel-area-86" class="">三里屯</li>
                      <li ka="sel-area-87" class="">世贸天阶</li>
                      <li ka="sel-area-88" class="">双桥</li>
                      <li ka="sel-area-89" class="">芍药居</li>
                      <li ka="sel-area-90" class="">三元桥</li>
                      <li ka="sel-area-91" class="">团结湖</li>
                      <li ka="sel-area-92" class="">甜水园</li>
                      <li ka="sel-area-93" class="">太阳宫</li>
                      <li ka="sel-area-94" class="">天竺</li>
                      <li ka="sel-area-95" class="">望京</li>
                      <li ka="sel-area-96" class="">王四营</li>
                      <li ka="sel-area-97" class="">西坝河</li>
                      <li ka="sel-area-98" class="">小关</li>
                      <li ka="sel-area-99" class="">小红门</li>
                      <li ka="sel-area-100" class="">小营</li>
                      <li ka="sel-area-101" class="">霄云路</li>
                      <li ka="sel-area-102" class="">姚家园</li>
                      <li ka="sel-area-103" class="">燕莎</li>
                      <li ka="sel-area-104" class="">永泰</li>
                      <li ka="sel-area-105" class="">亚运村</li>
                      <li ka="sel-area-106" class="">左家庄</li>
                      <li ka="sel-area-107" class="">中央别墅区</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="page-job-inner">
          <div class="page-job-content clearfix">
            <div class="job-list-wrapper">
              <div v-if="!is_close" class="subscribe-weixin-wrapper">
                <a href="javascript:" ka="subscription_close" class="close-btn" @click="is_close=true">
                  <i class="icon-close">
                  </i>
                </a>
                <div class="subscribe-weixin-inner">
                  <img src="https://img.bosszhipin.com/static/file/2022/05s3qgcgj11653987067425.png">
                  <h3>新职位发布时通知我</h3><p>订阅<em>【北京/算法】</em>相关岗位，新岗位上线实时通知，求职快人一步</p>
                </div>
              </div>
              <!---->
              <div class="search-job-result">
                <ul class="job-list-box">
                  <li v-for="job in list" ka="search_list_1" class="job-card-wrapper">
                    <div class="job-card-body clearfix">
                      <router-link :to="get_link_job(job.job_id, job)" class="job-card-left">
                        <div class="job-title clearfix">
                          <span class="job-name">{{job.job_name}}</span>
                          <span class="job-area-wrapper">
                                                    <span class="job-area">{{job.job_area}}</span>
                                                </span>
                        </div>
                        <div class="job-info clearfix"><span class="salary">{{job.job_salary}}</span>
                          <ul class="tag-list">
                            <!---->
                            <li v-for="item in job.job_info">{{ item }}</li>
                          </ul>
                          <div class="info-public">
                            {{job.recruiter[0]}}<em>{{ job.recruiter[1] }}</em>
                          </div>
                          <!-- <a href="javascript:;" ka="cpc_job_list_chat_1" class="start-chat-btn">立即沟通</a> -->
                          <!---->
                        </div>
                        <!---->
                      </router-link>
                      <div class="job-card-right">
<!--                        <div class="company-logo">-->
<!--                          <a href="" ka="search_list_company_1_custompage_logo">-->
<!--                            <img src="../images/字节跳动logo.jfif">-->
<!--                          </a>-->
<!--                        </div>-->
                        <div class="company-info">
                          <router-link :to="'/company/'+job.company_emailf">看公司简介</router-link>
                          <h3 class="company-name">
                            <router-link :to="get_link_company(job.company_email)" ka="search_list_company_1_custompage">{{ job.company_name }}</router-link>
                            <!---->
                          </h3>
                          <ul class="company-tag-list">
                            <li v-for="item in job.company_info">{{item}}</li>
                          </ul>
                        </div>
                      </div>
                    </div>
                    <!---->
                  </li>
                </ul>
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
  name: "joblist",
  props: ['search_str'],
  data() {
    return {
      search: "",

      username: '1',
      type: 'unlogin',

      beijing_: ['不限', '朝阳区', '海淀区', '大兴区', '丰台区', '昌平区', '东城区', '通州区', '西城区', '顺义区', '石景山区', '房山区',
        '门头沟区', '怀柔区', '密云区', '延庆区', '平谷区'],
      list: [
        {
          job_id: 1,
          job_name: '算法实习生',
          job_area: '北京·海淀区·知春路',
          job_salary: '400-800元/天',
          job_info: ['4天/周', '3个月', '本科'],
          recruiter: ['李女士', '安全主管'],
          re_id: "",
          company_email: 1,
          company_name: '字节跳动',
          company_info: ['互联网', 'A轮', '10000人以上'],
          // company_tag: "节日福利，加班补助，免费班车，补充医疗保险，年终奖，带薪年假，包吃，五险一金，定期体检，零食下午茶，住房补贴"
        }
      ],
      is_close: false
    }
  },
  mounted() {
    if (global.this_type !== 'unlogin') {
      this.get_username()
      this.type = global.this_token
    }
    this.get_job_list()
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
    get_job_list() {
      let that = this
      that.list = []

      this.$axios.post('companies/search_job_by_name', {
        position_name: this.search_str
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        res.data.job_list.forEach(
            (item) => {
              console.log(item)
              let _job_id = item.job_id
              let _recruiter = []
              let _id = item.recruiter_id
              let _job_name = item.position_name
              let _job_area = this.getProvince(item.position_address[0])
              let _job_salary = item.position_salary_from + "-" + item.position_salary_to + "K"
              let _job_info = []
              _job_info.push(this.experience(item.position_experience))
              _job_info.push(this.education(item.position_education))
              let _email = item.corporation_email
              let _company_name = []
              let _company_info = []

              this.$axios.post('companies/get_corporation_name', {
                email: _email
              }, {
                headers: {
                  'EMAIL': global.this_email,
                  'AUTHORIZATION': global.this_token
                }
              }).then((res) => {
                _company_name.push(res.data.corporation_abbreviation)
                this.$axios.post('companies/get_corporation_state_of_finance', {
                  email: _email
                }, {
                  headers: {
                    'EMAIL': global.this_email,
                    'AUTHORIZATION': global.this_token
                  }
                }).then((res) => {
                  _company_info.push(that.state_of_finance(res.data.corporation_state_of_finance))
                  _company_info.push(that.size_of_staff(res.data.corporation_size_of_staff))
                  _company_info.push(res.data.corporation_field)
                  this.$axios.post('companies/get_recruiter', {
                    email: _email,
                    id: _id
                  }, {
                    headers: {
                      'EMAIL': global.this_email,
                      'AUTHORIZATION': global.this_token
                    }
                  }).then((res) => {
                    _recruiter.push(res.data.recruiter_name)
                    _recruiter.push(res.data.recruiter_post)
                  })
                })
              })

              that.list.push({
                job_id: _job_id,
                recruiter: _recruiter,
                job_name: _job_name,
                job_area: _job_area,
                job_salary: _job_salary,
                job_info: _job_info,
                company_email: _email,
                company_name: _company_name[0],
                company_info: _company_info,
                re_id: _id
              })
              console.log(that.list)
            }
        )

      })
    },

    getProvince(province_code) {
      return CodeToText[province_code]
    },

    state_of_finance(str) {
      return str === 1 ? "已融资" : "未融资"
    },
    size_of_staff(str) {
      switch (str) {
        case 0:
          return "1-9"+"人"
        case 1:
          return "10-49"+"人"
        case 2:
          return "50-100"+"人"
        case 3:
          return "100-499"+"人"
        case 4:
          return "500-999"+"人"
        case 5:
          return "1000-4999"+"人"
        case 6:
          return "5000-9999"+"人"
        case 7:
          return "10000-30000"+"人"
        case 8:
          return "30000以上"+"人"
        default:
          return "default"
      }
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

    get_link_joblist(str) {
      return "/joblist/" + str
    },
    get_link_job(id, job) {
      return "/job/" + job.company_email + "/" + id + "/" + job.re_id
    },
    get_link_company(email) {
      return "/company/" + email
    },
    showup(){
      document.getElementById("droplist").style.display = "block";
      },
    disapear(){
      document.getElementById("droplist").style.display = "none";
    }
  },
  computed: {
    is_employee() {
      return global.this_type==='employee'
    },
    get_email() {
      return global.this_email
    },
  }
}
</script>

<style scoped>
@import "../assets/css/vender.css";
@import "../assets/css/app.css";
@import "../assets/css/tiwate.css";
</style>