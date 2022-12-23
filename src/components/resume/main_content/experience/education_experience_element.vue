<template>
  <div style="padding-left: 10px">
    <div style="padding-top: 5px; height: 25px">
      <div style="float: left; padding-right: 30px">
        <span style="font-size: 15px;color: #414a60; font-weight: bold">{{education_name}}</span>
      </div>
      <div style="float: left">
        <span style="font-size: 11px; color: #53cad0; font-weight: lighter">{{education_start}}至{{education_end}}</span>
      </div>
    </div>

    <div style="padding-top: 5px; height: 25px">
      <div style="float: left">
        <span style="font-size: 14px; font-weight: bold; color: #61687c">{{education_subject}}</span>
      </div>
      <div style="float: left; padding-left: 10px; padding-right: 10px">
        <span class="iconfont icon-shuxian" style="font-size: 15px;color: #414a60; font-weight: bold"></span>
      </div>
      <div style="float: left">
        <span style="font-size: 14px; font-weight: bold; color: #61687c">{{education_qualification}}</span>
      </div>
    </div>

    <div style="padding-top: 5px; padding-bottom: 3px">
      <span style="font-size: 14px; font-weight: bold; color: #61687c">内容：</span>
      <span style="font-size: 13px">{{education_experience}}</span>
    </div>

  </div>
</template>

<script>
import global from "../../../global.js";

export default {
  name: "education_experience_element",
  props: ['id'],
  data() {
    return {
      education_name: "",
      education_record: "-1",
      education_subject: "",
      education_start: "",
      education_end: "",
      education_experience: ""
    }
  },
  mounted() {
    this.init_education_name()
    this.init_education_record()
    this.init_education_subject()
    this.init_education_start()
    this.init_education_end()
    this.init_education_experience()
  },
  methods: {
    init_education_name() {
      let that = this
      that.$axios.post('people/get_education_name', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.education_name = res.data.education_name
      }).catch((res) => console.log(res))
    },
    init_education_record() {
      let that = this
      that.$axios.post('people/get_education_record', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.education_record = res.data.education_record
      }).catch((res) => console.log(res))
    },
    init_education_subject() {
      let that = this
      that.$axios.post('people/get_education_subject', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.education_subject = res.data.education_subject
      }).catch((res) => console.log(res))
    },
    init_education_start() {
      let that = this
      that.$axios.post('people/get_education_start', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.education_start = res.data.education_start
      }).catch((res) => console.log(res))
    },
    init_education_end() {
      let that = this
      that.$axios.post('people/get_education_end', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.education_end = res.data.education_end
      }).catch((res) => console.log(res))
    },
    init_education_experience() {
      let that = this
      that.$axios.post('people/get_education_experience', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.education_experience = res.data.education_experience
      }).catch((res) => console.log(res))
    },
  },
  computed: {
    education_qualification() {
      switch (this.education_record) {
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
      }
    }
  }
}
</script>

<style scoped>

</style>