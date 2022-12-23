<template>
  <div style="padding-left: 10px">
    <div style="padding-top: 5px; height: 25px">
      <div style="float: left; padding-right: 30px">
        <span style="font-size: 15px;color: #414a60; font-weight: bold">{{company_name}}</span>
      </div>
      <div style="float: left">
        <span style="font-size: 11px; color: #53cad0; font-weight: lighter">{{company_start}}至{{company_end}}</span>
      </div>
    </div>

    <div style="padding-top: 5px; height: 25px">
      <div v-if="company_field" style="float: left; padding-right: 50px">
        <span style="font-size: 15px;color: #414a60; font-weight: bold">{{company_field}}</span>
      </div>
      <div style="float: left">
        <span style="font-size: 15px;color: #414a60; font-weight: bold">{{company_position}}</span>
      </div>
    </div>

    <div style="padding-top: 5px; padding-bottom: 3px">
      <span style="font-size: 14px; font-weight: bold; color: #61687c">内容：</span>
      <span style="font-size: 13px">{{company_content}}</span>
    </div>

    <div v-if="company_achievement" style="padding-top: 5px; padding-bottom: 3px">
      <span style="font-size: 14px; font-weight: bold; color: #61687c">业绩：</span>
      <span style="font-size: 13px">{{company_achievement}}</span>
    </div>
  </div>
</template>

<script>
import global from "../../../global.js";

export default {
  name: "work_experience_element",
  props: ['id'],
  data() {
    return {
      company_name: "",
      company_field: "",
      company_position: "",
      company_start: "",
      company_end: "",
      company_content: "",
      company_achievement: ""
    }
  },
  mounted() {
    this.init_company_name()
    this.init_company_field()
    this.init_company_position()
    this.init_company_start()
    this.init_company_end()
    this.init_company_content()
    this.init_company_achievement()
  },
  methods: {
    init_company_name() {
      let that = this
      that.$axios.post('people/get_company_name', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.company_name = res.data.company_name
      }).catch((res) => console.log(res))
    },
    init_company_field() {
      let that = this
      that.$axios.post('people/get_company_field', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.company_field = res.data.company_field
      }).catch((res) => console.log(res))
    },
    init_company_position() {
      let that = this
      that.$axios.post('people/get_company_position', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.company_position = res.data.company_position
      }).catch((res) => console.log(res))
    },
    init_company_start() {
      let that = this
      that.$axios.post('people/get_company_start', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.company_start = res.data.company_start
      }).catch((res) => console.log(res))
    },
    init_company_end() {
      let that = this
      that.$axios.post('people/get_company_end', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.company_end = res.data.company_end
      }).catch((res) => console.log(res))
    },
    init_company_content() {
      let that = this
      that.$axios.post('people/get_company_content', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.company_content = res.data.company_content
      }).catch((res) => console.log(res))
    },
    init_company_achievement() {
      let that = this
      that.$axios.post('people/get_company_achievement', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.company_achievement = res.data.company_achievement
      }).catch((res) => console.log(res))
    },
  }
}
</script>

<style scoped>

</style>