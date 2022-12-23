<template>
  <div style="padding-bottom: 20px">
    <div style="padding: 12px 24px; background: #f9f9f9; border-radius: 10px 10px 0 0">
      <span>工作时间及福利</span>
    </div>
    <div :class="{move_on: !is_check}" @click="click_new">
      <div style="margin-left: 24px; padding-top: 15px">
        <div>
          <span style="color: #5dd5c8" class="iconfont icon-shijian"></span>
          <span style="padding-left: 10px; padding-bottom: 5px; font-size: 13px; font-weight: lighter">{{corporation_am_time}} - {{corporation_pm_time}}</span>
        </div>
      </div>
      <div style="margin-left: 24px; padding-top: 15px">
        <div>
          <span style="color: #5dd5c8" class="iconfont icon-xiuxi"></span>
          <span style="padding-left: 10px; padding-bottom: 5px; font-size: 13px; font-weight: lighter">{{ corporation_offwork }}</span>
        </div>
      </div>
    </div>

    <div :class="{move_on: !is_check}" @click="click_new_2">
      <div v-if="corporation_welfare_list.length!==0" style="margin-left: 20px">
        <ul style="padding-left: 0">
          <li @click="click_edit_2(item)" style="float: left; list-style-type: none; margin-right: 20px; margin-bottom: 6px; margin-top: 6px; padding: 3px 10px; border-radius: 4px; background: #f8f8f8" v-for="item in corporation_welfare_list">
            <div>
              <span style="font-size: 14px; color: #666666">{{item.content}}</span>
            </div>
          </li>
        </ul>
        <div style="clear:both;"></div>
      </div>
      <div v-else>
        <div style="height: 20px; margin-left: 30px; margin-top: 20px">
          <h5 @click="click_new_2">点击添加工作福利</h5>
        </div>
      </div>
    </div>

    <el-dialog v-if="!is_check" v-model="is_new" width="50%" title="修改工作时间">
      <div>
        <div style="width: 400px; padding-bottom: 30px; float: left; margin-right: 40px">
          <div class="information_title">
            <span class="information_title_str">工作时间：</span>
          </div>
          <div>
            <el-time-select format="HH:mm" v-model="edit_s_time" placeholder="Start time" />
            <el-time-select format="HH:mm" v-model="edit_e_time" placeholder="End time" />
          </div>
        </div>
        <div style="width: 330px; float: left; padding-bottom: 30px">
          <div class="information_title">
            <span class="information_title_str">休假方式：</span>
          </div>
          <div>
            <el-input v-model="edit_offwork" show-word-limit maxlength="10" />
          </div>
        </div>

        <div style="clear:both;"></div>
      </div>

      <div class="check">
        <div class="check_box_2" style="display: flex;align-items: center;text-align: center" @click="check_new">
          <label style="width: 90px; cursor: pointer">
            <span style="color: white">确定</span>
          </label>
        </div>
        <div class="check_box_1" style="display: flex;align-items: center;text-align: center" @click="finish_new">
          <label style="width: 90px; cursor: pointer">
            <span>取消</span>
          </label>
        </div>
      </div>
    </el-dialog>

    <el-dialog v-if="!is_check" v-model="edit_2" width="40%" title="修改福利">
      <div>
        <el-input v-model="edit_welfare" maxlength="10" placeholder="请输入贵公司人才发展信息" show-word-limit />
      </div>
      <div class="check">
        <div class="check_box_2" style="display: flex;align-items: center;text-align: center" @click="check_right_2">
          <label style="width: 90px; cursor: pointer">
            <span style="color: white">确定</span>
          </label>
        </div>
        <div class="check_box_1" style="display: flex;align-items: center;text-align: center" @click="check_finish_2">
          <label style="width: 90px; cursor: pointer">
            <span>取消</span>
          </label>
        </div>
        <div v-if="!is_new" class="check_box_3" style="display: flex;align-items: center;text-align: center" @click="check_delete_2">
          <label style="width: 90px; cursor: pointer">
            <span>删除</span>
          </label>
        </div>
      </div>
    </el-dialog>

    <el-dialog v-if="!is_check" v-model="new_3" width="40%" title="添加福利">
      <div>
        <el-input v-model="edit_welfare" maxlength="10" placeholder="请输入贵公司人才发展信息" show-word-limit />
      </div>
      <div class="check">
        <div class="check_box_2" style="display: flex;align-items: center;text-align: center" @click="check_new_2">
          <label style="width: 90px; cursor: pointer">
            <span style="color: white">确定</span>
          </label>
        </div>
        <div class="check_box_1" style="display: flex;align-items: center;text-align: center" @click="check_finish_2">
          <label style="width: 90px; cursor: pointer">
            <span>取消</span>
          </label>
        </div>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import global from "../global.js";

export default {
  name: "worktime_and_welfare",
  props: ['is_check'],
  data() {
    return {
      corporation_am_time: "09:00",
      corporation_pm_time: "14:00",
      corporation_offwork: "双休、不加班", //10个字以内,
      corporation_welfare_list: [
          {
            id: 1,
            content: "五险一金"
          },
        {
          id: 2,
          content: "加班补助"
        }
      ],

      edit_s_time: "",
      edit_e_time: "",
      edit_offwork: "", //10个字以内,
      edit_welfare: "",
      edit_record_welfare: "",
      is_new: false,
      edit_2: false,
      new_2: false,
      new_3: false,
      edit_id: -1
    }
  },
  mounted() {
    this.init_worktime()
    this.init_welfare()
  },
  methods: {
    init_worktime() {
      let that = this
      that.$axios.post('companies/get_corporation_am_time', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.corporation_am_time = res.data.corporation_am_time
        that.corporation_pm_time = res.data.corporation_pm_time
        that.corporation_offwork = res.data.corporation_offwork
      }).catch((res) => console.log(res))
    },
    init_welfare() {
      let that = this
      this.corporation_welfare_list = []
      that.$axios.post('companies/get_welfare_list', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.corporation_welfare_list = res.data.corporation_welfare_list
      }).catch((res) => console.log(res))
    },

    click_new() {
      this.is_new = true
      this.edit_s_time = this.corporation_am_time
      this.edit_e_time = this.corporation_pm_time
      this.edit_offwork = this.corporation_offwork
    },
    check_new() {
      if (this.edit_s_time === "" || this.edit_e_time === "") {
        this.$message("请输入工作时间")
      }
      else if (this.edit_offwork === "") {
        this.$message("请输入休假方式")
      }
      else {
        let that = this
        that.$axios.post('companies/upd_corporation_am_time', {
          email: global.this_email,
          corporation_am_time: that.edit_s_time,
          corporation_pm_time: that.edit_e_time,
          corporation_offwork: that.edit_offwork,
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then(() =>{
          that.init_worktime()
          this.finish_new()
        })
      }
    },
    finish_new() {
      this.is_new = false
    },
    click_edit_2(item) {
      this.edit_2 = true
      this.edit_id = item.id
      this.edit_welfare = item.content
      this.edit_record_welfare = item.content
    },
    click_new_2() {
      if (!this.edit_2) {
        this.new_3 = true
        this.edit_welfare = ""
      }
    },
    check_finish_2() {
      this.edit_2 = false
      this.new_3 = false
    },
    check_right_2() {
      // 向后端传递修改（或新建）后的数据
      if (this.edit_welfare === "") {
        this.$message("请不要修改为空")
      }
      else {
        let that = this
        that.$axios.post('companies/upd_welfare', {
          email: global.this_email,
          id: this.edit_id,
          content: that.edit_welfare,
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then(() =>{
          that.init_welfare()
          this.check_finish_2()
        })
      }
    },
    check_delete_2() {
      // 向后端传递删除的数据
      let that = this
      that.$axios.post('companies/del_welfare_list', {
        email: global.this_email,
        id: that.edit_id,
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then(() =>{
        that.init_welfare()
        this.check_finish_2()
      })
    },
    check_new_2() {
      // 向后端传递修改（或新建）后的数据
      if (this.edit_welfare === "") {
        this.$message("请不要修改为空")
      }
      else {
        let that = this
        that.$axios.post('companies/add_welfare_list', {
          email: global.this_email,
          content: that.edit_welfare,
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then(() =>{
          that.init_welfare()
          this.check_finish_2()
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