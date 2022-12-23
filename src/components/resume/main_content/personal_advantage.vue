<template>
  <div class="advantage">
    <div style="padding-top: 15px" >
      <div style="float: left; height: 20px">
        <span class="iconfont icon-shuxian picture v_line"></span>
      </div>
      <span style="font-size: 18px; color: #414a60">个人优势</span>

      <span v-if="is_move_on" style="float: right; padding-right: 50px; font-size: 14px; font-weight: lighter; color: slategrey">编辑</span>
      <label v-if="is_move_on" class="iconfont icon-bianji" style="float: right; padding-right: 7px; padding-top: 1px"></label>
    </div>
    <div style="padding: 15px 50px 15px 10px">
      <div :class="{po: is_move_on}" style="width: 634px; border-radius: 5px; padding-left: 10px" @mouseover="move_on" @mouseout="move_out" @click="$emit('click_2')">
        <span class="auto_new_line" style="font-size: 16px;font-weight: lighter; padding: 7px">{{my_advantage}}</span>
      </div>
    </div>
  </div>
</template>

<script>
import global from "../../global.js";

export default {
  name: "own_advantage",
  data() {
    return {
      my_advantage: "",
      is_move_on: false
    }
  },
  mounted() {
    this.init_advantage()
  },
  methods: {
    init_advantage() {
      let that = this
      that.$axios.post('people/get_my_advantage', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_advantage = res.data.my_advantage
      }).catch((res) => console.log(res))
    },

    move_on() {
      this.is_move_on = true
    },
    move_out() {
      this.is_move_on = false
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

.auto_new_line {
  display: inline-block;
  width: 620px;
  word-break: break-all;
  white-space: normal;
}

.po {
  cursor: pointer;
  background: white;
}

</style>