<template>
  <div class="information_edit">
    <div style="padding-top: 20px; padding-bottom: 20px">
      <span style="color: #414a60; font-size: 16px">编辑个人优势</span>
    </div>
    <div style="padding-right: 50px">
      <el-input v-model="my_advantage" type="textarea" rows="9" placeholder="请输入您的优势" maxlength="200" show-word-limit />
    </div>
    <div class="check">
      <div class="check_box_2" style="display: flex;align-items: center;text-align: center" @click="check_right(); check_finish()">
        <label style="width: 90px; cursor: pointer">
          <span style="color: white">确定</span>
        </label>
      </div>
      <div class="check_box_1" style="display: flex;align-items: center;text-align: center" @click="check_finish">
        <label style="width: 90px; cursor: pointer">
          <span>取消</span>
        </label>
      </div>
    </div>
  </div>
</template>

<script>
import global from "../../global.js";

export default {
  name: "personal_advantage_edit",
  data() {
    return {
      my_advantage: "sfd"
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
    check_finish() {
      // 向前端输送完成编辑信号
      this.$emit("edit_finish_2")
    },
    check_right() {
      // 向后端传递修改后的数据
      if (this.my_advantage === '') {
        this.$message("请输入您的个人优势")
      }
      else {
        let that = this
        that.$axios.post('people/upd_my_advantage', {
          email: global.this_email,
          my_advantage: that.my_advantage
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then(() =>{
          that.check_finish()
        })
      }
    }
  },
}
</script>

<style scoped>

.information_edit {
  padding-left: 40px;
  background: rgba(248, 253, 253, 0.9);
}

.check {
  height: 60px;
}

.check_box_1 {
  width: 90px;
  margin-right: 35px;
  margin-top: 10px;
  border: 1px solid gray;
  background: white;
  height: 32px;
  float: right;
}

.check_box_2 {
  width: 90px;
  margin-right: 50px;
  margin-top: 10px;
  border: 1px solid gray;
  background: #5dd5c8;
  height: 32px;
  float: right;
}

</style>