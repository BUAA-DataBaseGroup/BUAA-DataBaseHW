<template>
  <div>
    <!-- 导航条开始 -->
    <div id="header">
      <div class="inner home-inner">
        <div class="mylogo">
          <router-link to="/" title="提瓦特招聘">
            <span>提瓦特招聘</span>
          </router-link>
        </div>
        <div class="nav">
          <ul style="height: 49px">
            <li style="height: 49px" class="cur"><router-link to="/" style="height: 49px">首页</router-link></li>
            <li style="height: 49px" class=""><router-link to="/joblist/C++工程师" style="height: 49px">职位</router-link></li>
            <li style="height: 49px" class=""><a style="height: 49px" href="#">校园</a></li>
            <li style="height: 49px" class=""><a style="height: 49px" href="#">公司</a></li>
            <li style="height: 49px" class=""><a style="height: 49px" href="#">咨询</a></li>
            <li style="height: 49px" class=""><a style="height: 49px" href="#">百科</a></li>
          </ul>
        </div>
        <div class="user-nav">
          <div class="btns">
            <router-link to="/employee_login" rel="nofollow" ka="nlp_resume_upload" class="link-sign-resume" title="上传简历，解析内容，完善注册">我要找工作</router-link>
            <router-link to="/company_login" rel="nofollow" ka="header-geek" class="link-sign-resume" title="上传简历，解析内容，完善注册">我要招聘</router-link>
<!--            <a href="login.html" ka="header-register" class="btn btn-outline">个人注册登录</a>-->
<!--            <a href="register.html" ka="header-register" class="btn btn-outline">招聘者注册登录</a>-->
          </div>
        </div>
      </div>
    </div>
    <!-- 导航条结束 -->
    <!-- 搜索条开始 -->
  <!--</div>-->
    <!--快速注册-->
    <!--快速注册 end-->

    <!-- 搜索 -->
    <div class="column-search-panel search-panel-new">
      <div class="inner home-inner">
        <div class="search-box">
          <div>
            <div>
              <el-input v-model="search_s" style="height: 50px;width: 750px;" placeholder="搜索感兴趣的工作"></el-input>
              <button class="btn btn-search" @click="jumpto">搜索</button>
            </div>
          </div>
          <div class="search-hot">
            <b>热门职位:</b>
            <router-link v-for="item in link_00" :to="get_link(item)">{{item}}</router-link>
          </div>
        </div>
      </div>
    </div>
    <!-- 搜索条结束 -->
    <!-- 主体开始 -->
    <div id="main" class="inner home-inner">
      <div class="home-box">
        <div class="home-sider">
          <div class="home-job-menu">
            <div class="job-menu-wrapper">
              <dl class="">
                <dd>
                  <i class="iboss-right-fill"></i>
                  <b>技术</b>
                  <router-link v-for="item in link_hot_1" :to="get_link(item)">{{item}}</router-link>
                </dd>
                <div class="menu-sub">
                  <p class="menu-article">技术</p>
                  <ul>
                    <li>
                      <h4>后端开发</h4>
                      <div class="text">
                        <router-link v-for="item in link_1001" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                    <li>
                      <h4>移动开发</h4>
                      <div class="text">
                        <router-link v-for="item in link_1002" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                    <li>
                      <h4>测试</h4>
                      <div class="text">
                        <router-link v-for="item in link_1003" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                    <li>
                      <h4>运维/技术支持</h4>
                      <div class="text">
                        <router-link v-for="item in link_1004" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                    <li>
                      <h4>数据</h4>
                      <div class="text">
                        <router-link v-for="item in link_1005" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                    <li>
                      <h4>项目管理</h4>
                      <div class="text">
                        <router-link v-for="item in link_1006" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                    <li>
                      <h4>硬件开发</h4>
                      <div class="text">
                        <router-link v-for="item in link_1008" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                    <li>
                      <h4>前端开发</h4>
                      <div class="text">
                        <router-link v-for="item in link_1009" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                    <li>
                      <h4>通信</h4>
                      <div class="text">
                        <router-link v-for="item in link_1010" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                    <li>
                      <h4>电子/半导体</h4>
                      <div class="text">
                        <router-link v-for="item in link_1014" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                    <li>
                      <h4>高端技术职位</h4>
                      <div class="text">
                        <router-link v-for="item in link_1007" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                    <li>
                      <h4>人工智能</h4>
                      <div class="text">
                        <router-link v-for="item in link_1013" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                    <li>
                      <h4>销售技术支持</h4>
                      <div class="text">
                        <router-link v-for="item in link_1012" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                    <li>
                      <h4>其他技术职位</h4>
                      <div class="text">
                        <router-link v-for="item in link_1011" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                  </ul>
                </div>
              </dl>
              <dl class="">
                <dd>
                  <i class="iboss-right-fill"></i>
                  <b>产品</b>
                  <router-link v-for="item in link_hot_2" :to="get_link(item)">{{item}}</router-link>
                </dd>
                <div class="menu-sub">
                  <p class="menu-article">产品</p>
                  <ul>
                    <li>
                      <h4>产品经理</h4>
                      <div class="text">
                        <router-link v-for="item in link_1101" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                    <li>
                      <h4>高端产品职位</h4>
                      <div class="text">
                        <router-link v-for="item in link_1103" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                    <li>
                      <h4>其他产品职位</h4>
                      <div class="text">
                        <router-link v-for="item in link_1104" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                  </ul>
                </div>
              </dl>
              <dl class="">
                <dd>
                  <i class="iboss-right-fill"></i>
                  <b>高级管理</b>
                  <router-link v-for="item in link_hot_5" :to="get_link(item)">{{item}}</router-link>
                </dd>
                <div class="menu-sub">
                  <p class="menu-article">高级管理</p>
                  <ul>
                    <li>
                      <h4>高级管理职位</h4>
                      <div class="text">
                        <router-link v-for="item in link_1504" :to="get_link(item)">{{item}}</router-link>
                      </div>
                    </li>
                  </ul>
                </div>
              </dl>
            </div>
          </div>
        </div>
        <div class="home-main">
          <div class="slider-box">
            <div class="promotion-main" data-id="9981efc0def856b01XJz3g~~">
              <table data-sort="sortDisabled">
                <tbody>
                <tr class="firstRow">
                  <td colspan="2" rowspan="2"><router-link :to='get_link("大数据工程师")' style="white-space: normal;" target="_blank" rel="noopener" ka="https://www.zhipin.com/job_detail/?query=大数据工程师"><img src="https://img.bosszhipin.com/beijin/upload/image/20220704/a75e120f323f706ce73149adcdb97228.png" alt="" width="522" height="226" /></router-link></td>
                  <td width="307"><router-link :to='get_link("设计师")' target="_blank" rel="noopener" vip="0" ka="https://www.zhipin.com/job_detail/?query=设计师"><img src="https://img.bosszhipin.com/beijin/upload/image/20220704/8a19f6b6ab0d102560c868d313153623.png" alt="" width="260" height="112" /></router-link><br /></td>
                </tr>
                <tr>
                  <td width="307"><router-link :to='get_link("游戏策划")' target="_blank" rel="noopener" vip="0" ka="https://www.zhipin.com/job_detail/?query=游戏策划"><img src="https://img.bosszhipin.com/beijin/upload/image/20220704/c98b8db2e3dfac8c65fa121e39fb74d4.png" alt="" width="260" height="112" /></router-link><br /></td>
                </tr>
                <tr>
                  <td colspan="2" rowspan="1"><router-link :to='get_link("算法工程师")' target="_blank" rel="noopener" vip="0" ka="https://www.zhipin.com/job_detail/?query=算法工程师"><img src="https://img.bosszhipin.com/beijin/upload/image/20220704/d707890b49693206a3c9a0fe3823e9b1.png" alt="" width="522" height="112" /></router-link><br /></td>
                  <td width="307"><router-link :to='get_link("java工程师")' target="_blank" href="" rel="noopener" vip="0" ka="https://www.zhipin.com/job_detail/?query=java工程师"><img src="https://img.bosszhipin.com/beijin/upload/image/20220704/f7c18d678ac4121bb6e000dba7e1fe2a.png" alt="" width="260" height="112" /></router-link><br /></td>
                </tr>
                </tbody>
              </table>
              <p><br style="white-space: normal;" /></p>
              <p><br style="white-space: normal;" /></p>
              <p><br /></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "homepage_unlogin",
  data() {
    return {
      search_select: 0,
      search_s: "",

      link_00: ['C++工程师', '智能驾驶系统工程师', '需求分析工程师', '系统策划', '后端开发', '风控', '心理咨询师'],

      link_hot_1: ['Java', 'PHP', '前端开发工程师', '算法工程师'],
      link_1001: ['Java', 'C++', 'PHP', 'C', 'C#', '.NET', 'Hadoop', 'Python', 'Delphi', 'VB', 'Perl', 'Ruby', 'Node.js',
        'Golang', 'Erlang', '语音/视频/图形开发', '数据采集', '全栈工程师', 'GIS工程师', '后端开发'],
      link_1002: ['技术美术', 'Android', 'iOS', 'Flash开发', 'JavaScript', 'U3D', 'Cocos', 'UE4', '移动开发'],
      link_1003: ['测试工程师', '自动化测试', '功能测试', '性能测试', '测试开发', '移动端测试', '游戏测试', '硬件测试', '软件测试', '渗透测试'],
      link_1004: ['运维工程师', '运维开发工程师', '网络工程师', '系统工程师', 'IT技术支持', '系统管理员', '网络安全', '系统安全', 'DBA'],
      link_1005: ['数据', 'ETL工程师', '数据仓库', '数据开发', '数据挖掘', '数据分析师', '数据架构师'],
      link_1006: ['项目经理/主管', '项目助理', '项目专员', '实施顾问', '实施工程师', '需求分析工程师', '硬件项目经理'],
      link_1008: ['光学工程师', '硬件工程师', '嵌入式', '自动化', '单片机', '电路设计', '驱动开发', '系统集成', 'FPGA开发', 'DSP开发', 'ARM开发', 'PCB工艺', '射频工程师'],
      link_1009: ['前端开发工程师', 'Flash开发'],
      link_1010: ['通信技术工程师', '通信研发工程师', '数据通信工程师', '移动通信工程师', '电信网络工程师', '电信交换工程师', '有线传输工程师',
        '无线/射频通信工程师', '通信电源工程师', '通信标准化工程师', '通信项目专员', '通信项目经理', '核心网工程师', '通信测试工程师', '通信设备工程师',
        '光通信工程师', '光传输工程师', '光网络工程师'],
      link_1014: ['电气工程师', '电气设计工程师', '电子工程师', '集成电路IC设计', 'FAE', 'IC验证工程师'],
      link_1007: ['高端技术职位', '技术经理', '技术总监', '测试经理', '架构师', 'CTO', '运维总监', '技术合伙人'],
      link_1013: ['人工智能', '数据挖掘', '搜索算法', '自然语言处理', '推荐算法', '算法工程师', '智能驾驶系统工程师', '反欺诈/风控算法',
        '机器学习', '深度学习', '语音识别', '图像识别', '算法研究员'],
      link_1012: ['销售技术支持', '售前技术支持', '售后技术支持'],
      link_1011: ['其他技术职位'],

      link_hot_2: ['产品经理', '高级产品管理岗', '数据产品经理'],
      link_1101: ['AI产品经理', '产品经理', '网页产品经理', '移动产品经理', '产品助理', '数据产品经理', '电商产品经理', '游戏策划', '产品专员', '硬件产品经理'],
      link_1103: ['高级产品管理岗', '游戏制作人'],
      link_1104: ['其他产品职位'],

      link_hot_5: ['总裁/总经理/CEO', '分公司/代表处负责人'],
      link_1504: ['高级管理职位', '总裁/总经理/CEO', '副总裁/副总经理/VP', '分公司/代表处负责人', '区域负责人(辖多个分公司)',
        '总助/CEO助理/董事长助理', '联合创始人', '董事会秘书'],
    }
  },
  methods: {
    let_str_right_route(str) {
      let new_s = ""
      for (let c of str) {
        if (c === '/') {
          new_s = new_s + '_'
        }
        else {
          new_s = new_s + c
        }
      }
      return new_s
    },
    get_link(str) {
      return "/joblist/" + this.let_str_right_route(str)
    },
    showup() {
      document.getElementById("droplist").style.display = "block";
    },
    disapear() {
      document.getElementById("droplist").style.display = "none";
    },
    jumpto() {
      this.$router.push('/joblist/'+this.search_s)
    }
  }
}
</script>

<style scoped>
@import "../assets/css/index_main.css";
@import "../assets/css/tiwate.css";

</style>