<template>
  <div style="padding-left: 10px">
    <div style="padding-top: 5px; height: 25px">
      <div style="float: left; padding-right: 30px">
        <span style="font-size: 15px;color: #414a60; font-weight: bold">{{item_name}}</span>
      </div>
      <div style="float: left">
        <span style="font-size: 11px; color: #53cad0; font-weight: lighter">{{item_start}}至{{item_end}}</span>
      </div>
    </div>

    <div style="padding-top: 5px; padding-bottom: 3px">
      <span style="font-size: 14px; font-weight: bold; color: #61687c">{{item_role}}</span>
    </div>

    <div style="padding-top: 5px; padding-bottom: 3px">
      <span style="font-size: 14px; font-weight: bold; color: #61687c">内容：</span>
      <span style="font-size: 13px">{{item_description}}</span>
    </div>

    <div v-if="item_achievement" style="padding-top: 5px; padding-bottom: 3px">
      <span style="font-size: 14px; font-weight: bold; color: #61687c">业绩：</span>
      <span style="font-size: 13px">{{item_achievement}}</span>
    </div>

    <div v-if="item_link" style="padding-top: 5px; padding-bottom: 3px">
      <span style="font-size: 14px; font-weight: bold; color: #61687c">项目链接：</span>
      <span style="font-size: 13px">{{item_link}}</span>
    </div>
  </div>
</template>

<script>
import global from "../../../global.js";

export default {
  name: "item_experience_element",
  props: ['id'],
  data() {
    return {
      item_name: "",
      item_role: "",
      item_link: "",
      item_start: "",
      item_end: "",
      item_description: "",
      item_achievement: ""
    }
  },
  mounted() {
    this.init_item_name()
    this.init_item_role()
    this.init_item_link()
    this.init_item_start()
    this.init_item_end()
    this.init_item_description()
    this.init_item_achievement()
  },
  methods: {
    init_item_name() {
      let that = this
      that.$axios.post('people/get_item_name', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.item_name = res.data.item_name
      }).catch((res) => console.log(res))
    },
    init_item_role() {
      let that = this
      that.$axios.post('people/get_item_role', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.item_role = res.data.item_role
      }).catch((res) => console.log(res))
    },
    init_item_link() {
      let that = this
      that.$axios.post('people/get_item_link', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.item_link = res.data.item_link
      }).catch((res) => console.log(res))
    },
    init_item_start() {
      let that = this
      that.$axios.post('people/get_item_start', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.item_start = res.data.item_start
      }).catch((res) => console.log(res))
    },
    init_item_end() {
      let that = this
      that.$axios.post('people/get_item_end', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.item_end = res.data.item_end
      }).catch((res) => console.log(res))
    },
    init_item_description() {
      let that = this
      that.$axios.post('people/get_item_description', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.item_description = res.data.item_description
      }).catch((res) => console.log(res))
    },
    init_item_achievement() {
      let that = this
      that.$axios.post('people/get_item_achievement', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.item_achievement = res.data.item_achievement
      }).catch((res) => console.log(res))
    },
  },
}
</script>

<style scoped>

</style>