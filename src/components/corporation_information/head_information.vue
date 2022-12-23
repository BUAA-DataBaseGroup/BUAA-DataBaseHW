<template>
  <div style="padding-left: 200px; padding-top: 30px; padding-bottom: 30px; background: #414a60">
    <div :class="{edit: is_move_on&&!is_check, move_on: !is_check}" style="margin-right: 200px; padding-bottom: 5px; padding-left: 5px" @mouseover="is_move_on=true" @mouseout="is_move_on=false" @click="click_edit">
      <div style="margin-bottom: 10px">
        <span style="font-size: 40px; font-weight: bolder; color: white">{{corporation_abbreviation}}</span>
        <span v-if="is_move_on&&!is_check" style="float: right; padding-right: 50px; font-size: 16px; font-weight: lighter" :style="{color: edit_color}">编辑</span>
        <label v-if="is_move_on&&!is_check" class="iconfont icon-bianji" style="font-size: 16px; float: right; padding-right: 7px; padding-top: 1px" :style="{color: edit_color}"></label>
      </div>
      <div>
        <span v-if="corporation_state_of_finance !== -1" style="color:white;">{{ state_of_finance }}</span>
        <span v-if="corporation_state_of_finance !== -1" class="iconfont icon-yuandian" style="color: white; padding-left: 5px; padding-right: 5px"></span>
        <span v-if="corporation_size_of_staff !== -1" style="color:white;">{{ size_of_staff }}人</span>
        <span v-if="corporation_size_of_staff !== -1" class="iconfont icon-yuandian" style="color: white; padding-left: 5px; padding-right: 5px"></span>
        <span v-if="corporation_field" style="color:white;">{{ corporation_field }}</span>
      </div>
    </div>

    <el-dialog v-if="!is_check" v-model="is_edit" width="50%" title="修改基本信息">
      <div style="margin-left: 40px">
        <div>
          <div style="padding-bottom: 20px; float: left; margin-right: 40px">
            <div class="information_title">
              <span class="information_title_str">公司简称：</span>
            </div>
            <div>
              <el-input v-model="edit_name" style="width: 302px; height: 30px" maxlength="10" show-word-limit />
            </div>
          </div>
          <div style="padding-bottom: 20px">
            <div class="information_title">
              <span class="information_title_str">融资情况：</span>
            </div>
            <div>
              <el-select v-model="edit_state_of_finance" placeholder="请选择贵公司融资情况">
                <el-option :value="0" label="未融资">未融资</el-option>
                <el-option :value="1" label="已融资">已融资</el-option>
              </el-select>
            </div>
          </div>
          </div>
        <div>
          <div style="padding-bottom: 20px; float: left; margin-right: 40px">
            <div class="information_title">
              <span class="information_title_str">所在领域：</span>
            </div>
            <div>
              <el-input v-model="edit_field" placeholder="请输入贵公司所在领域" style="width: 302px; height: 30px" maxlength="20" show-word-limit />
            </div>
          </div>
          <div style="padding-bottom: 20px">
            <div class="information_title">
              <span class="information_title_str">公司规模：</span>
            </div>
            <div>
                <el-select v-model="edit_size_of_staff" placeholder="请选择贵公司规模">
                <el-option :value="0" label="1-9人" />
                <el-option :value="1" label="10-49人" />
                <el-option :value="2" label="50-99人" />
                <el-option :value="3" label="100-499人" />
                <el-option :value="4" label="500-999人" />
                <el-option :value="5" label="1000-4999人" />
                <el-option :value="6" label="5000-9999人" />
                <el-option :value="7" label="10000-30000人" />
                <el-option :value="8" label="30000以上人" />
              </el-select>
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
      </div>
    </el-dialog>

  </div>
</template>

<script>
import global from "../global.js";

export default {
  name: "head_information",
  props: ['is_check'],
  data() {
    return {
      corporation_name: "",
      corporation_abbreviation: "",
      corporation_state_of_finance: "", // -1为默认，0未，1已
      corporation_size_of_staff: "", // -1为默认
      corporation_field: "",
      is_move_on: false,
      is_edit: false,
      edit_color: "#53cac3",
      // 需要初始化
      edit_name: "",
      edit_state_of_finance: "", // 打开修改后，如果记录为-1，则设为""
      edit_size_of_staff: "",
      edit_field: ""
    }
  },
  computed: {
    state_of_finance() {
      return this.corporation_state_of_finance === 1 ? "已融资" : "未融资"
    },
    size_of_staff() {
      switch (this.corporation_size_of_staff) {
        case 0:
          return "1-9"
        case 1:
          return "10-49"
        case 2:
          return "50-100"
        case 3:
          return "100-499"
        case 4:
          return "500-999"
        case 5:
          return "1000-4999"
        case 6:
          return "5000-9999"
        case 7:
          return "10000-30000"
        case 8:
          return "30000以上"
        default:
          return "default"
      }
    }
  },
  mounted() {
    this.init_corporation_name()
    this.init_corporation_state_of_finance()

  },
  methods: {
    init_corporation_name() {
      let that = this
      that.$axios.post('companies/get_corporation_name', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.corporation_name = res.data.corporation_name
        that.corporation_abbreviation = res.data.corporation_abbreviation
      }).catch((res) => console.log(res))
    },
    init_corporation_state_of_finance() {
      let that = this
      that.$axios.post('companies/get_corporation_state_of_finance', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.corporation_state_of_finance = res.data.corporation_state_of_finance
        that.corporation_size_of_staff = res.data.corporation_size_of_staff
        that.corporation_field = res.data.corporation_field
      }).catch((res) => console.log(res))
    },

    click_edit() {
      this.is_edit=true
      this.edit_name = this.corporation_abbreviation
      this.edit_state_of_finance = this.corporation_state_of_finance === -1 ? "" : this.corporation_state_of_finance
      this.edit_size_of_staff = this.corporation_size_of_staff === -1 ? "" : this.corporation_size_of_staff
      this.edit_field = this.corporation_field
    },
    check_finish() {
      this.is_edit=false
    },
    check_right() {
      // 向后端传递修改（或新建）后的数据
      if (this.edit_name === "") {
        this.$message("请输入公司全称")
      }
      else if (this.edit_state_of_finance === "") {
        this.$message("请输入公司融资情况")
      }
      else if (this.edit_size_of_staff === "") {
        this.$message("请输入公司规模")
      }
      else if (this.edit_field === "") {
        this.$message("请输入公司所在领域")
      }
      else {
        let that = this
        that.$axios.post('companies/upd_corporation_name', {
          email: global.this_email,
          corporation_name: that.corporation_name,
          corporation_abbreviation: that.edit_name
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then(() =>{
          that.$axios.post('companies/upd_corporation_state_of_finance', {
            email: global.this_email,
            corporation_state_of_finance: that.edit_state_of_finance,
            corporation_size_of_staff: that.edit_size_of_staff,
            corporation_field: that.edit_field
          }, {
            headers: {
              'EMAIL': global.this_email,
              'AUTHORIZATION': global.this_token
            }
          }).then(() =>{
            that.init_corporation_name()
            that.init_corporation_state_of_finance()
            that.check_finish()
          })
        })
      }
    }
  }
}
</script>

<style scoped>

.edit {
  background: #61687c;
}

.information_title_str {
  font-size: 17px;
  font-weight: bold;
}

.information_title {
  padding-bottom: 8px;
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

.move_on {
  cursor: pointer;
}

</style>