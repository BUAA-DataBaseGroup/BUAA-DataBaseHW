<template>
  <div style="padding: 24px; background: white; margin-bottom: 16px; border-radius: 10px" @mouseover="is_point=true" @mouseout="is_point=false">
    <div style="height: 56px">
      <div :class="{move_on: !is_check}" style="width: 560px; float: left;"  @click="edit">
        <div :class="{point_color: is_point&&!is_check}" style="height: 22px; margin-bottom: 8px">
          <span style="font-weight: 400">{{position_name}} [{{getProvince(position_address[0])}}]</span>
        </div>
        <div style="height: 24px">
          <span style="color: red; float: left; font-size: 18px; margin-right: 8px">{{position_salary_from}}-{{position_salary_to}}K</span>
          <div style="float: left; padding: 2px 8px; background: rgb(247, 247, 247); margin-right: 8px">
            <span style="font-size: 13px; color: #666666">{{experience}}</span>
          </div>
          <div style="float: left; padding: 2px 8px; background: rgb(247, 247, 247)">
            <span style="font-size: 13px; color: #666666">{{education}}</span>
          </div>
        </div>
      </div>
      <div style="float: left">
        <div style="float: left; margin-right: 16px">
          <img alt="" style="height: 48px; width: 48px; border-radius: 24px" src="../../../assets/boss.png">
        </div>
        <div style="float: left">
          <div style="height: 22px; margin-bottom: 6px">
            <span style="font-size: 16px; font-weight: 500">{{boss_name}}</span>
          </div>
          <div style="height: 20px">
            <span style="font-size: 14px; color: rgb(102, 102, 102)">{{boss_post}}</span>
          </div>
        </div>
      </div>
    </div>

    <el-dialog v-if="!is_check" v-model="is_edit" title="修改招聘信息" width="47%">
      <div>
        <div style="padding-bottom: 20px; float: left; margin-right: 40px">
          <div class="information_title">
            <span class="information_title_str">工作名称：</span>
          </div>
          <div>
            <el-input v-model="edit_name" style="width: 302px; height: 30px" maxlength="10" show-word-limit />
          </div>
        </div>
        <div style="padding-bottom: 20px">
          <div class="information_title">
            <span class="information_title_str">工作地点：</span>
          </div>
          <div>
            <el-cascader size="large" :options="options" v-model="edit_address"></el-cascader>
          </div>
        </div>
      </div>

      <div>
        <div style="padding-bottom: 20px; float: left; margin-right: 40px">
          <div class="information_title">
            <span class="information_title_str">工作经验要求：</span>
          </div>
          <div>
            <el-select v-model="edit_experience" style="width: 302px; height: 36px">
              <el-option :value="0" label="在校生">在校生</el-option>
              <el-option :value="1" label="应届生">应届生</el-option>
              <el-option :value="2" label="一年以内">一年以内</el-option>
              <el-option :value="3" label="1-3年">1-3年</el-option>
              <el-option :value="4" label="3-5年">3-5年</el-option>
              <el-option :value="5" label="5-10年">5-10年</el-option>
              <el-option :value="6" label="10年以上">10年以上</el-option>
            </el-select>
          </div>
        </div>
        <div style="padding-bottom: 20px">
          <div class="information_title">
            <span class="information_title_str">教育程度要求：</span>
          </div>
          <div>
            <el-select v-model="edit_education" style="width: 302px; height: 36px">
              <el-option :value="0" label="初中及以下">初中及以下</el-option>
              <el-option :value="1" label="中专/中技">中专/中技</el-option>
              <el-option :value="2" label="高中">高中</el-option>
              <el-option :value="3" label="大专">大专</el-option>
              <el-option :value="4" label="本科">本科</el-option>
              <el-option :value="5" label="硕士">硕士</el-option>
              <el-option :value="6" label="博士">博士</el-option>
            </el-select>
          </div>
        </div>
      </div>

      <div>
        <div style="padding-bottom: 20px; float: left; margin-right: 40px; width: 302px">
          <div class="information_title">
            <span class="information_title_str">提供薪资范围（千）：</span>
          </div>
          <div>
            <el-input-number v-model="edit_salary_from" size="small" :min="1" :max="edit_salary_to" />
            <span style="margin: 0 10px">至</span>
            <el-input-number v-model="edit_salary_to" size="small" :min="edit_salary_from" />
          </div>
        </div>
        <div style="padding-bottom: 20px">
          <div class="information_title">
            <span class="information_title_str">招聘Boss：</span>
          </div>
          <div>
            <el-select v-model="edit_boss_id">
              <el-option
                v-for="item in all_boss"
                :key="item.id"
                :label="item.name"
                :value="item.id"
                />
            </el-select>
          </div>
        </div>
      </div>

      <div>
        <div style="padding-bottom: 20px; margin-right: 40px">
          <div class="information_title">
            <span class="information_title_str">岗位描述：</span>
          </div>
          <div>
            <el-input style="width: 100%" maxlength="1500" type="textarea" show-word-limit v-model="edit_description" />
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

  </div>
</template>

<script>
import { regionData, CodeToText } from 'element-china-area-data'
import global from "../../global.js";

export default {
  name: "position_element",
  props: ['position_id', 'is_check'],
  emits: ['element_delete'],
  data() {
    return {
      options: regionData,

      position_name: "",
      position_address: ["", "", ""],
      position_experience: -1, //默认-1，0-6
      position_education: -1,  //默认-1，0-6
      position_salary_from: 1,
      position_salary_to: 3,
      position_boss_id: "",
      position_description: "",

      boss_name: '',
      boss_post: "",

      is_point: false,
      is_edit: false,

      edit_name: "",
      edit_address: [],
      edit_experience: -1, //默认-1，0-6
      edit_education: -1,  //默认-1，0-6
      edit_salary_from: 1,
      edit_salary_to: 3,
      edit_boss_id: "",
      all_boss: [{
        id: 1,
        name: "xk"
      }],
      edit_description: ""
    }
  },
  computed: {
    experience() {
      switch (this.position_experience) {
        case 0:
          return "在校生"
        case 1:
          return "应届生"
        case 2:
          return "一年以内"
        case 3:
          return "1-3年"
        case 4:
          return "3-5年"
        case 5:
          return "5-10年"
        case 6:
          return "10年以上"
        default:
          return "error"
      }
    },
    education() {
      switch (this.position_experience) {
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
        default:
          return "error"
      }
    }
  },
  mounted() {
    this.init_()
  },
  methods: {
    init_() {
      let that = this
      // console.log(this.position_id)
      that.$axios.post('companies/get_job', {
        email: global.this_email,
        id: this.position_id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.position_name = res.data.position_name
        that.position_address = res.data.position_address
        that.position_experience = res.data.position_experience
        that.position_education = res.data.position_education
        that.position_salary_from = res.data.position_salary_from
        that.position_salary_to = res.data.position_salary_to
        that.position_boss_id = res.data.recruiter_id
        that.position_description = res.data.position_description
        that.$axios.post('companies/get_recruiter', {
          email: global.this_email,
          id: that.position_boss_id
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then((res) => {
          that.boss_name = res.data.recruiter_name
          that.boss_post = res.data.recruiter_post
        }).catch((res) => console.log(res))
      }).catch((res) => console.log(res))

      this.all_boss = []
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
              that.all_boss.push({
                id: item.id,
                name: item.recruiter_name
              })
            }
        )
      }).catch((res) => console.log(res))
    },

    getProvince(province_code) {
      return CodeToText[province_code]
    },
    edit() {
      this.is_edit = true
      this.edit_name = this.position_name
      this.edit_address = this.position_address
      this.edit_experience = this.position_experience
      this.edit_education = this.position_education
      this.edit_salary_from = this.position_salary_from
      this.edit_salary_to = this.position_salary_to
      this.edit_boss_id = this.position_boss_id
      this.edit_description = this.position_description
    },
    check_finish() {
      this.is_edit = false
    },
    check_right() {
      // 向后端传递修改（或新建）后的数据
      if (this.edit_name === "" || this.edit_address === "") {
        this.$message("请不要修改为空")
      }
      else {
        let that = this
        that.$axios.post('companies/upd_job', {
          email: global.this_email,
          id: this.position_id,
          recruiter_id: that.edit_boss_id,
          position_name: that.edit_name,
          position_address: that.edit_address,
          position_experience: that.edit_experience,
          position_education: that.edit_education,
          position_salary_from: that.edit_salary_from,
          position_salary_to: that.edit_salary_to,
          position_description: that.edit_description,
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
      let that = this
      that.$axios.post('companies/del_job', {
        email: global.this_email,
        id: this.position_id,
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then(() =>{
        this.$emit('element_delete')
        this.check_finish()
      })
    }
  }
}
</script>

<style scoped>

.point_color {
  color: rgb(2, 170, 171);
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