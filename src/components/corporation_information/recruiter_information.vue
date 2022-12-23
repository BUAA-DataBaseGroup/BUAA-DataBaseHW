<template>
  <div style="padding-bottom: 20px" @mouseover="is_over=true" @mouseout="is_over=false">
    <div style="padding: 12px 24px; background: #f9f9f9; border-radius: 10px 10px 0 0">
      <span>招聘Boss</span>
      <div v-if="!is_check" style="float: right; cursor: pointer;padding-left: 20px" @click="click_new">
        <span style="float: right; font-size: 14px; font-weight: lighter; color: slategrey">添加</span>
        <label class="iconfont icon-tianjia" style="float: right; padding-right: 7px; padding-top: 1px; cursor: pointer" ></label>
      </div>
    </div>

    <div style="padding: 3px 7px">
      <div v-for="id in recruiter_id_list">
        <recruiter_element :is_check="is_check" :id="id" @element_delete="check_delete" />
      </div>
    </div>

    <el-dialog v-model="is_add" title="添加Boss信息" width="47%">
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
      </div>
    </el-dialog>
  </div>
</template>

<script>
import recruiter_element from "./position_and_recruiter_element/recruiter_element.vue";
import global from "../global.js";

export default {
  name: "recruiter_information",
  props: ['is_check'],
  data() {
    return {
      recruiter_id_list: [],

      is_over: false,
      is_add: false,
      edit_name: "",
      edit_post: ""
    }
  },
  components: [
      recruiter_element
  ],
  beforeMount() {
    this.init_()
  },
  methods: {
    init_() {
      let that = this
      this.recruiter_id_list = []
      that.$axios.post('companies/get_recruiter_list', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        res.data.corporation_recruiter_list.forEach(
            (item) => {
              that.recruiter_id_list.push(item.id)
            }
        )
      }).catch((res) => console.log(res))
    },

    check_delete() {
      this.init_()
    },
    click_new() {
      this.edit_name = ""
      this.edit_post = ""
      this.is_add = true
    },
    check_finish() {
      this.is_add = false
    },
    check_right() {
      // 向后端传递修改（或新建）后的数据
      if (this.edit_name === "" || this.edit_post === "") {
        this.$message("请不要提交空信息")
      } else {
        // 向后端传输，在从后端获得新的list
        let that = this
        that.$axios.post('companies/add_recruiter_list', {
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
    }
  }
}
</script>

<style scoped>

.first_row {
  width: 350px;
}

.information_title_str {
  font-size: 17px;
}

.information_title {
  padding-bottom: 8px;
}

.line {
  height: 80px;
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

</style>