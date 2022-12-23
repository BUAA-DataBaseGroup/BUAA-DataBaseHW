<template>
  <div class="advantage">
    <div style="padding-top: 15px" >
      <div style="float: left; height: 20px">
        <span class="iconfont icon-shuxian picture v_line"></span>
      </div>
      <span style="font-size: 18px; color: #414a60">期望职位</span>

      <span v-if="is_move_on" style="float: right; padding-right: 50px; font-size: 14px; font-weight: lighter; color: slategrey">编辑</span>
      <label v-if="is_move_on" class="iconfont icon-bianji" style="float: right; padding-right: 7px; padding-top: 1px"></label>
    </div>
    <div style="padding: 15px 50px 15px 10px">
      <div :class="{po: is_move_on}" style="width: 634px; border-radius: 5px; padding-left: 10px" @mouseenter="move_on" @mouseout="move_out" @click="$emit('click_3')">
        <span v-if="is_all_null">请输入您的期望职位</span>

        <span v-if="my_expect_work_position" class="iconfont icon-lingdai picture"></span>
        <span v-if="my_expect_work_position" class="word">{{my_expect_work_position}}</span>
        <span v-if="my_expect_work_position" class="iconfont icon-vertical_line divide"></span>

        <span v-if="is_salary_not_null" class="iconfont icon-jinqian picture"></span>
        <span v-if="is_salary_not_null" class="word">{{my_expect_salary}}k</span>
        <span v-if="is_salary_not_null" class="iconfont icon-vertical_line divide"></span>

        <span v-if="my_expect_work_field" class="iconfont icon-hangye picture"></span>
        <span v-if="my_expect_work_field" class="word">{{my_expect_work_field}}</span>
        <span v-if="my_expect_work_field" class="iconfont icon-vertical_line divide"></span>

        <span v-if="my_expect_work_place" class="iconfont icon-didian picture"></span>
        <span v-if="my_expect_work_place" class="word">{{my_expect_work_place}}</span>

      </div>
    </div>
  </div>
</template>

<script>
import global from "../../global.js";

export default {
  name: "personal_expect",
  data() {
    return {
      my_expect_work_type: 0, // 0 -> 未选择，1 -> 全职，2 -> 兼职
      my_expect_work_place: "", // 6char
      my_expect_work_position: "",  // 10char
      my_expect_work_field: "", // 10char
      my_expect_salary: 1,
      is_move_on: false
    }
  },
  mounted() {
    this.init_expect_work_type()
    this.init_expect_work_place()
    this.init_expect_work_position()
    this.init_expect_work_field()
    this.init_expect_salary()
  },
  methods: {
    init_expect_work_type() {
      let that = this
      that.$axios.post('people/get_my_expect_work_type', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_expect_work_type = res.data.my_expect_work_type
      }).catch((res) => console.log(res))
    },
    init_expect_work_place() {
      let that = this
      that.$axios.post('people/get_my_expect_work_place', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_expect_work_place = res.data.my_expect_work_place
      }).catch((res) => console.log(res))
    },
    init_expect_work_position() {
      let that = this
      that.$axios.post('people/get_my_expect_work_position', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_expect_work_position = res.data.my_expect_work_position
      }).catch((res) => console.log(res))
    },
    init_expect_work_field() {
      let that = this
      that.$axios.post('people/get_my_expect_work_field', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_expect_work_field = res.data.my_expect_work_field
      }).catch((res) => console.log(res))
    },
    init_expect_salary() {
      let that = this
      that.$axios.post('people/get_my_expect_salary', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_expect_salary = res.data.my_expect_salary
      }).catch((res) => console.log(res))
    },

    move_on() {
      this.is_move_on = true
    },
    move_out() {
      this.is_move_on = false
    }
  },
  computed: {
    is_salary_not_null() {
      return this.my_expect_work_type === 1 && this.my_expect_salary !== -1
    },
    is_all_null() {
      return !this.is_salary_not_null && this.my_expect_work_position === "" && this.my_expect_work_field === "" && this.my_expect_work_place === ""
    }
  }
}
</script>

<style scoped>
.advantage {
  background: white;
  padding-left: 40px;
}

.v_line {
  font-weight: bolder;
  font-size: 20px;
  color: #53cac3;
}

.po {
  cursor: pointer;
  background: white;
}

.divide {
  font-size: 12px;
  font-weight: lighter;
  padding-left: 15px;
  padding-right: 8px;
}

.picture {
  padding-right: 10px;
}

</style>