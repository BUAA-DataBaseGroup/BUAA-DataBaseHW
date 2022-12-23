<template>
  <div :class="{point_background: is_point, move_on: !is_check}" style="border-radius: 8px; margin-bottom: 13px; margin-top: 3px" @mouseover="is_point=true" @mouseout="is_point=false" @click="check_click">
    <div style="padding-left: 10px; margin-bottom: 5px">
      <span :class="{point_color: is_point}">{{recruiter_name}}</span>
      <span :class="{point_color: is_point, color: !is_point}" class="iconfont icon-shuxian"></span>
      <span :class="{point_color: is_point, color: !is_point}" >{{recruiter_post}}</span>
    </div>
    <div v-if="recruiter_duty_name_list.length" style="padding-left: 10px">
      <span :class="{point_color: is_point, color: !is_point}"  style="font-size: 13px">正在招聘“{{recruiter_duty_name_str}}”等职位</span>
    </div>
  </div>

  <el-dialog v-if="!is_check" v-model="is_edit" title="修改Boss信息" width="47%">
    <div>
      <div style="padding-bottom: 20px; float: left; margin-right: 40px">
        <div class="information_title">
          <span class="information_title_str">Boss名称：</span>
        </div>
        <div>
          <el-input v-model="edit_name" style="width: 302px; height: 30px" maxlength="4" show-word-limit />
        </div>
      </div>
      <div style="padding-bottom: 20px">
        <div class="information_title">
          <span class="information_title_str">Boss职务：</span>
        </div>
        <div>
          <el-input v-model="edit_post" style="width: 302px; height: 30px" maxlength="8" show-word-limit />
        </div>
      </div>
    </div>
    <div class="check">
      <div class="check_box_2" style="display: flex;align-items: center;text-align: center" @click="check_right">
        <label style="width: 90px; cursor: pointer">
          <span style="color: white">确定</span>
        </label>
      </div>
      <div class="check_box_1" style="display: flex;align-items: center;text-align: center" @click="check_finish">
        <label style="width: 90px; cursor: pointer">
          <span>取消</span>
        </label>
      </div>
      <div class="check_box_3" style="display: flex;align-items: center;text-align: center" @click="check_delete">
        <label style="width: 90px; cursor: pointer">
          <span>删除</span>
        </label>
      </div>
    </div>
  </el-dialog>
</template>

<script>
import global from "../../global.js";

export default {
  name: "recruiter_element",
  props: ['id', 'is_check'],
  emits: ['element_delete'],
  data() {
    return {
      recruiter_name: "",
      recruiter_post: "",

      recruiter_duty_name_list: [],
      is_point: false,
      is_edit: false,
      edit_name: "",
      edit_post: ""
    }
  },
  computed: {
    recruiter_duty_name_str() {
      let str = "";
      for (let item of this.recruiter_duty_name_list) {
        str += item + "，"
      }
      return str.substring(0, str.length-1)
    }
  },
  mounted() {
    this.init_()
  },
  methods: {
    init_() {
      let that = this
      that.$axios.post('companies/get_recruiter', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.recruiter_name = res.data.recruiter_name
        that.recruiter_post = res.data.recruiter_post
      }).catch((res) => console.log(res))
    },
    init_job_list() {
      let that = this
      that.$axios.post('companies/get_recruiter_job_list', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.recruiter_duty_name_list = res.data.recruiter_job_list
      }).catch((res) => console.log(res))
    },

    check_click() {
      this.is_edit = true
      this.edit_name = this.recruiter_name
      this.edit_post = this.recruiter_post
    },
    check_finish() {
      this.is_edit = false
    },
    check_right() {
      // 向后端传递修改（或新建）后的数据
      if (this.edit_name === "" || this.edit_post === "") {
        this.$message("请不要修改为空")
      }
      else {
        let that = this
        that.$axios.post('companies/upd_recruiter', {
          email: global.this_email,
          id: this.id,
          recruiter_name: that.edit_name,
          recruiter_post: that.edit_post,
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then(() =>{
          that.init_()
          this.check_finish()
        })
      }
    },
    check_delete() {
      // 向后端传递删除的数据
      if (this.recruiter_duty_name_list.length !== 0) {
        this.$message("请先将该Boss负责招聘信息更换Boss后在进行删除")
      }
      else {
        let that = this
        that.$axios.post('companies/del_recruiter_list', {
          email: global.this_email,
          id: this.id,
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then(() =>{
          that.$emit('element_delete')
          this.check_finish()
        })
      }
    }
  }
}
</script>

<style scoped>

.point_color {
  color: rgb(2, 170, 171);
}

.color {
  color: rgb(34,128,126)
}

.point_background {
  background: #fafafa;
}

.information_title_str {
  font-size: 17px;
}

.information_title {
  padding-bottom: 8px;
}

.check {
  height: 60px;
}

.check_box_1 {
  width: 60px;
  margin-right: 10px;
  margin-top: 30px;
  border: 1px solid gray;
  background: white;
  height: 32px;
  float: right;
}

.check_box_2 {
  width: 60px;
  margin-right: 10px;
  margin-top: 30px;
  border: 1px solid gray;
  background: #5dd5c8;
  height: 32px;
  float: right;
}

.check_box_3 {
  width: 60px;
  margin-right: 10px;
  margin-top: 30px;
  border: 1px solid gray;
  background: orangered;
  height: 32px;
  float: right;
}

.move_on {
  cursor: pointer;
}

</style>