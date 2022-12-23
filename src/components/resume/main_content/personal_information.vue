<template>
  <div class="information">
    <div style="padding-top: 13px; padding-bottom: 25px">
      <span style="font-size: 23px">{{my_name}}</span>
    </div>
    <div v-if="my_date_of_first_work && my_education !== -1 && my_status !== -1" class="line">
      <span v-if="working_time" class="iconfont icon-gongwenbao picture"></span>
      <span v-if="working_time" class="word">{{working_time}}年经验</span>
      <span v-if="working_time" class="iconfont icon-vertical_line divide"></span>

      <span v-if="my_education !== -1" class="iconfont icon-education-1-copy picture"></span>
      <span v-if="my_education !== -1" class="word">{{education_}}</span>
      <span v-if="my_education !== -1" class="iconfont icon-vertical_line divide"></span>

      <span v-if="my_status !== -1" class="iconfont icon-zaizhi picture"></span>
      <span v-if="my_status !== -1" class="word">{{status_}}</span>
    </div>
    <div class="line">
      <span v-if="my_date_of_first_work" class="iconfont icon-shijian picture"></span>
      <span v-if="my_date_of_first_work" class="word">{{my_date_of_first_work}}</span>
      <span v-if="my_date_of_first_work" class="iconfont icon-vertical_line divide"></span>

      <span v-if="my_tel" class="iconfont icon-dianhua" style="padding-right: 3px"></span>
      <span v-if="my_tel" class="word">{{my_tel}}</span>
      <span v-if="my_tel" class="iconfont icon-vertical_line divide"></span>

<!--      <span v-if="my_wechat" class="iconfont icon-weixin picture"></span>-->
      <span v-if="my_wechat" class="iconfont icon-youxiang picture"></span>
      <span v-if="my_wechat" class="word">{{my_wechat}}</span>
      <span v-if="my_wechat" class="iconfont icon-vertical_line divide"></span>

      <span class="iconfont icon-youxiang picture"></span>
      <span class="word">{{my_email}}</span>

      <span v-if="enter" style="float: right; padding-right: 50px; font-size: 14px; font-weight: lighter" :style="{color: edit_color}" @mouseover="move_enter_edit" @mouseleave="move_out_edit">编辑</span>
      <label v-if="enter" class="iconfont icon-bianji" style="float: right; padding-right: 7px; padding-top: 1px"></label>
    </div>
  </div>
</template>

<script>
import global from "../../global.js";

export default {
  name: "personal_information",
  data() {
    return {
      my_email: "",

      my_name: "徐凯",
      my_education: -1, //0-6
      my_status: -1,
      my_date_of_first_work: "",
      my_tel: "",
      my_wechat: "",

      edit_color: "slategrey"
    }
  },
  props: [
      'enter'
  ],
  mounted() {
    this.my_email = global.this_email
    // this.my_education = this.init('my_education')
    this.init_name()
    this.init_status()
    this.init_date_of_first_work()
    this.init_wechat()
    this.init_birth()
    this.init_tel()
  },
  methods: {
    init_name() {
      let that = this
      that.$axios.post('people/get_my_name', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_name = res.data.my_name
      }).catch((res) => console.log(res))
    },
    init_status() {
      let that = this
      that.$axios.post('people/get_my_status', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_status = res.data.my_status
      }).catch((res) => console.log(res))
    },
    init_date_of_first_work() {
      let that = this
      that.$axios.post('people/get_my_date_of_first_work', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_date_of_first_work = res.data.my_date_of_first_work
      }).catch((res) => console.log(res))
    },
    init_wechat() {
      let that = this
      that.$axios.post('people/get_my_wechat', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_wechat = res.data.my_wechat
      }).catch((res) => console.log(res))
    },
    init_tel() {
      let that = this
      that.$axios.post('people/get_my_tel', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_tel = res.data.my_tel
      }).catch((res) => console.log(res))
    },
    init_birth() {
      let that = this
      that.$axios.post('people/get_my_birth', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_birth = res.data.my_birth
      }).catch((res) => console.log(res))
    },
    move_enter_edit() {
      this.edit_color = "#5dd5c8"
    },
    move_out_edit() {
      this.edit_color = "slategrey"
    }
  },
  computed: {
    working_time() {
      let now_yy = new Date().getFullYear()
      let now_mm = new Date().getMonth() + 1
      let yy = parseInt(this.my_date_of_first_work.substring(0,4))
      let mm = parseInt(this.my_date_of_first_work.substring(5,7))

      if (now_mm - mm >= 0) {
        return now_yy - yy + 1
      }
      else {
        return now_yy - yy
      }
    },
    education_() {
      switch (this.my_education) {
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
    status_() {
      switch (this.my_status) {
        case 0:
          return "离职-随时到岗"
        case 1:
          return "在职-暂不考虑"
        case 2:
          return "在职-考虑机会"
        case 3:
          return "在职-月内到岗"
        default:
          return "error"
      }
    }
  }
}
</script>

<style scoped>
.information {
  height: 130px;
  padding-left: 40px;

  background: white;
}

.line {
  padding-bottom: 5px;
}

.picture {
  padding-right: 10px;
}

.word {
  font-size: 14px;
  color: #414a60;
}

.divide {
  font-size: 12px;
  font-weight: lighter;
  padding-left: 15px;
  padding-right: 8px;
}

</style>