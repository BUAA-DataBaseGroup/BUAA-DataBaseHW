<template>
  <div>
    <div style="margin-bottom: 20px;height: 70px; background: white; border-radius: 10px">
      <div style="float: left;margin-right: 50px; margin-left: 30px">
        <div style="padding-bottom: 5px">
          <span style="padding-left: 20px">请选择工作地点</span>
        </div>
        <el-cascader style="width: 140px" :options="options" v-model="choose_address" placeholder="工作地点" />
      </div>
      <div style="float: left;margin-right: 50px">
        <div style="padding-bottom: 5px">
          <span style="padding-left: 5px">请选择工作经验要求</span>
        </div>
        <el-select v-model="choose_experience" style="width: 140px" placeholder="经验要求">
          <el-option :value="-1" label="不限">不限</el-option>
          <el-option :value="0" label="在校生">在校生</el-option>
          <el-option :value="1" label="应届生">应届生</el-option>
          <el-option :value="2" label="一年以内">一年以内</el-option>
          <el-option :value="3" label="1-3年">1-3年</el-option>
          <el-option :value="4" label="3-5年">3-5年</el-option>
          <el-option :value="5" label="5-10年">5-10年</el-option>
          <el-option :value="6" label="10年以上">10年以上</el-option>
        </el-select>
      </div>
      <div style="float: left;margin-right: 50px">
        <div style="padding-bottom: 5px">
          <span style="padding-left: 5px">请选择教育程度要求</span>
        </div>
        <el-select v-model="choose_education" style="width: 140px" placeholder="学历要求">
          <el-option :value="-1" label="不限">不限</el-option>
          <el-option :value="0" label="初中及以下">初中及以下</el-option>
          <el-option :value="1" label="中专/中技">中专/中技</el-option>
          <el-option :value="2" label="高中">高中</el-option>
          <el-option :value="3" label="大专">大专</el-option>
          <el-option :value="4" label="本科">本科</el-option>
          <el-option :value="5" label="硕士">硕士</el-option>
          <el-option :value="6" label="博士">博士</el-option>
        </el-select>
      </div>
      <div style="float: left;">
        <div style="padding-bottom: 5px">
          <span style="padding-left: 17px">请选择薪资范围</span>
        </div>
        <el-select v-model="choose_salary" style="width: 140px" placeholder="学历要求">
          <el-option :value="-1" label="不限">不限</el-option>
          <el-option :value="0" label="3K以下">3K以下</el-option>
          <el-option :value="1" label="3-5K">3-5K</el-option>
          <el-option :value="2" label="5-10K">5-10K</el-option>
          <el-option :value="3" label="10-20K">10-20K</el-option>
          <el-option :value="4" label="20-50K">20-50K</el-option>
          <el-option :value="5" label="50K">50K</el-option>
        </el-select>
      </div>
      <div v-if="!is_check" style="float: right; cursor: pointer; margin-right: 20px; margin-top: 20px" @click="click_new">
        <span style="float: right; font-size: 14px; font-weight: lighter; color: slategrey">添加</span>
        <label class="iconfont icon-tianjia" style="float: right; padding-right: 7px; padding-top: 1px; cursor: pointer" ></label>
      </div>
    </div>

    <div>
      <position_element :is_check="is_check" v-for="id in position_id_list" :position_id="id" @element_delete="check_delete(id)" />
    </div>

    <el-dialog v-if="!is_check" v-model="is_add" title="添加招聘信息" width="47%">
      <div>
        <div style="padding-bottom: 20px; float: left; margin-right: 40px">
          <div class="information_title">
            <span class="information_title_str">工作名称：</span>
          </div>
          <div>
            <el-input v-model="edit_name" style="width: 302px; height: 30px" :maxlength="10" show-word-limit placeholder="请填写工作名称" />
          </div>
        </div>
        <div style="padding-bottom: 20px">
          <div class="information_title">
            <span class="information_title_str">工作地点：</span>
          </div>
          <div>
            <el-cascader size="large" :options="options" v-model="edit_address" placeholder="请选择工作地点" />
          </div>
        </div>
      </div>

      <div>
        <div style="padding-bottom: 20px; float: left; margin-right: 40px">
          <div class="information_title">
            <span class="information_title_str">工作经验要求：</span>
          </div>
          <div>
            <el-select v-model="edit_experience" style="width: 302px; height: 36px" placeholder="请选择工作经验要求">
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
            <el-select v-model="edit_education" style="width: 302px; height: 36px" placeholder="请选择学历要求">
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
            <el-select v-model="edit_boss_id" placeholder="请选择招聘boss">
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
            <el-input style="width: 100%" maxlength="1500" type="textarea" show-word-limit v-model="edit_description" placeholder="请填写岗位描述" />
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
import position_element from "./position_and_recruiter_element/position_element.vue";
import { regionDataPlus } from 'element-china-area-data';
import global from "../global.js";

export default {
  name: "positions_information",
  props: ['is_check'],
  data() {
    return {
      choose_address: [],
      choose_experience: -1,
      choose_education: -1,
      choose_salary: -1,

      position_id_list: [],

      options: regionDataPlus,
      selectedOptions : [],

      is_add: false,
      edit_name: "",
      edit_address: [],
      edit_experience: -1, //默认-1，0-6
      edit_education: -1,  //默认-1，0-6
      edit_salary_from: 1,
      edit_salary_to: 2,
      edit_boss_id: "",
      all_boss: [{
        id: 1,
        name: "xk"
      }],
      edit_description: ""
    }
  },
  beforeMount() {
    this.init_()
    this.init_allBoss()
  },
  methods: {
    init_() {
      let that = this
      this.position_id_list = []
      that.$axios.post('companies/get_corporation_job_list', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        res.data.corporation_job_list.forEach(
            (item) => {
              that.position_id_list.push(item.job_id)
            }
        )
      }).catch((res) => console.log(res))
    },
    init_allBoss() {
      this.all_boss = []
      let that = this
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

    check_delete() {
      this.init_()
    },
    click_new() {
      this.edit_name = ""
      this.edit_address = ""
      this.edit_experience = ""
      this.edit_education = ""
      this.edit_salary_from = 1
      this.edit_salary_to = 2
      this.edit_boss_id = ""
      this.edit_description = ""
      this.is_add = true
    },
    check_finish() {
      this.is_add = false
    },
    check_right() {
      // 向后端传递修改（或新建）后的数据
      if (this.edit_name === "" || this.edit_address === ""|| this.edit_experience === ""|| this.edit_education === ""||
          this.edit_salary_from === ""|| this.edit_salary_to === ""|| this.edit_boss_id === ""|| this.edit_description === "") {
        this.$message("请不要修改为空")
      }
      else {
        let that = this
        that.$axios.post('companies/add_job', {
          email: global.this_email,
          id: that.edit_boss_id,
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
          that.check_finish()
          that.init_()
        })
      }
    }
  },
  computed: {
    choose_addr_() {
      if (this.choose_address.length !== 3 || this.choose_address[2] === '') {
        return -1
      }
      else {
        return this.choose_address[2]
      }
    }
  },
  watch: {
    choose_address(now, old) {
      if (now !== old) {
        console.log(this.choose_addr_)
        let that = this
        this.position_id_list = []
        that.$axios.post('companies/search_job', {
          email: global.this_email,
          position_address: this.choose_addr_,
          position_experience: this.choose_experience,
          position_education: this.choose_education,
          position_salary: this.choose_salary,
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then((res) => {
          res.data.job_list.forEach(
              (item) => {
                that.position_id_list.push(item.job_id)
              }
          )
        }).catch((res) => console.log(res))
      }
    },
    choose_experience(now, old) {
      if (now !== old) {
        let that = this
        this.position_id_list = []
        that.$axios.post('companies/search_job', {
          email: global.this_email,
          position_address: this.choose_addr_,
          position_experience: this.choose_experience,
          position_education: this.choose_education,
          position_salary: this.choose_salary,
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then((res) => {
          res.data.job_list.forEach(
              (item) => {
                that.position_id_list.push(item.job_id)
              }
          )
        }).catch((res) => console.log(res))
      }
    },
    choose_education(now, old) {
      if (now !== old) {
        let that = this
        this.position_id_list = []
        that.$axios.post('companies/search_job', {
          email: global.this_email,
          position_address: this.choose_addr_,
          position_experience: this.choose_experience,
          position_education: this.choose_education,
          position_salary: this.choose_salary,
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then((res) => {
          res.data.job_list.forEach(
              (item) => {
                that.position_id_list.push(item.job_id)
              }
          )
        }).catch((res) => console.log(res))
      }
    },
    choose_salary(now, old) {
      if (now !== old) {
        let that = this
        this.position_id_list = []
        that.$axios.post('companies/search_job', {
          email: global.this_email,
          position_address: this.choose_addr_,
          position_experience: this.choose_experience,
          position_education: this.choose_education,
          position_salary: this.choose_salary,
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then((res) => {
          res.data.job_list.forEach(
              (item) => {
                that.position_id_list.push(item.job_id)
              }
          )
        }).catch((res) => console.log(res))
      }
    }
  },
  components: {
    position_element
  }
}
</script>

<style scoped>

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