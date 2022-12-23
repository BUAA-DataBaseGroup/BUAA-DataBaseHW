<template>
  <div class="information_edit">
    <div style="padding-top: 20px; padding-bottom: 20px">
      <span style="color: #414a60; font-size: 16px">编辑教育经历</span>
    </div>

    <div class="information">
      <div class="line">
        <div class="first_row" style="float: left">
          <div class="information_title">
            <span class="information_title_str">学校名称</span>
          </div>
          <div style="width: 302px">
            <el-input v-model="education_name" placeholder="请输入您的学校名称" maxlength="20" show-word-limit />
          </div>
        </div>
        <div style="float: left">
          <div class="information_title">
            <span class="information_title_str">学历</span>
          </div>
          <div style="width: 302px">
            <el-select v-model="education_record" style="width: 302px; height: 36px" placeholder="请选择您学习所获学历">
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

      <div class="line">
        <div class="first_row" style="float: left">
          <div class="information_title">
            <span class="information_title_str">专业</span>
          </div>
          <div style="width: 302px">
            <el-input v-model="education_subject" placeholder="请输入您的专业" maxlength="20" show-word-limit />
          </div>
        </div>
      </div>

      <div class="line">
        <div class="first_row" style="float: left">
          <div class="information_title">
            <span class="information_title_str">学习时间</span>
          </div>
          <div style="width: 302px">
            <el-date-picker v-model="education_time" type="monthrange" value-format="YYYY-MM" range-separator="至" start-placeholder="开始时间" end-placeholder="结束时间" />
          </div>
        </div>
      </div>

      <div style="padding-bottom: 15px; width: 652px">
        <div class="information_title">
          <span class="information_title_str">在校经历（选填）</span>
        </div>
        <div>
          <el-input v-model="education_experience" type="textarea" rows="7" resize="none" placeholder="请输入您的在校经历" maxlength="1500" show-word-limit />
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
      <div v-if="!is_new" class="check_box_3" style="display: flex;align-items: center;text-align: center" @click="check_delete">
        <label style="width: 90px; cursor: pointer">
          <span>删除</span>
        </label>
      </div>
    </div>
  </div>
</template>

<script>
import global from "../../../global.js";

export default {
  name: "education_experience_edit_element",
  props: ['id', 'is_new'],
  emits: ['edit_finish_6'],
  data() {
    return {
      education_name: "",
      education_record: "",
      education_subject: "",
      education_time: ["", ""],
      education_experience: ""
    }
  },
  computed: {
    education_start() {
      return this.education_time.at(0)
    },
    education_end() {
      return this.education_time.at(1)
    }
  },
  mounted() {
    if (this.is_new) {
      this.education_name = ""
      this.education_record = ""
      this.education_subject = ""
      this.education_time = ["", ""]
      this.education_experience = ""
    }
    else {
      this.init_education_name()
      this.init_education_record()
      this.init_education_subject()
      this.init_education_start()
      this.init_education_end()
      this.init_education_experience()
    }
  },
  methods: {
    init_education_name() {
      let that = this
      that.$axios.post('people/get_education_name', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.education_name = res.data.education_name
      }).catch((res) => console.log(res))
    },
    init_education_record() {
      let that = this
      that.$axios.post('people/get_education_record', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.education_record = res.data.education_record
      }).catch((res) => console.log(res))
    },
    init_education_subject() {
      let that = this
      that.$axios.post('people/get_education_subject', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.education_subject = res.data.education_subject
      }).catch((res) => console.log(res))
    },
    init_education_start() {
      let that = this
      that.$axios.post('people/get_education_start', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.education_time[0] = res.data.education_start
      }).catch((res) => console.log(res))
    },
    init_education_end() {
      let that = this
      that.$axios.post('people/get_education_end', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.education_time[1] = res.data.education_end
      }).catch((res) => console.log(res))
    },
    init_education_experience() {
      let that = this
      that.$axios.post('people/get_education_experience', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.education_experience = res.data.education_experience
      }).catch((res) => console.log(res))
    },

    check_finish() {
      // 向前端输送完成编辑信号
      this.$emit("edit_finish_6")
    },
    check_right() {
      // 向后端传递修改（或新建）后的数据
      if (this.education_name === "") {
        this.$message("请输入公司名称")
      }
      else if (this.education_record === -1) {
        this.$message("请输入公司所属行业")
      }
      else if (this.education_subject === "") {
        this.$message("请输入职位名称")
      }
      else if (this.education_time[0] === '' || this.education_time[1] === '') {
        this.$message("请输入在职时间")
      }
      else {
        let that = this
        if (this.is_new) {
          that.$axios.post('people/add_my_education_list', {
            email: global.this_email,
            education_name: this.education_name,
            education_record: this.education_record,
            education_subject: this.education_subject,
            education_start: this.education_start,
            education_end: this.education_end,
            education_experience: this.education_experience,
          }, {
            headers: {
              'EMAIL': global.this_email,
              'AUTHORIZATION': global.this_token
            }
          }).then(() =>{
            that.check_finish()
          })
        }
        else {
          that.$axios.post('people/upd_education_name', {
            email: global.this_email,
            id: this.id,
            education_name: this.education_name,
          }, {
            headers: {
              'EMAIL': global.this_email,
              'AUTHORIZATION': global.this_token
            }
          }).then(() =>{
            that.$axios.post('people/upd_education_record', {
              email: global.this_email,
              id: this.id,
              education_record: this.education_record,
            }, {
              headers: {
                'EMAIL': global.this_email,
                'AUTHORIZATION': global.this_token
              }
            }).then(() =>{
              that.$axios.post('people/upd_education_subject', {
                email: global.this_email,
                id: this.id,
                education_subject: this.education_subject,
              }, {
                headers: {
                  'EMAIL': global.this_email,
                  'AUTHORIZATION': global.this_token
                }
              }).then(() =>{
                that.$axios.post('people/upd_education_start', {
                  email: global.this_email,
                  id: this.id,
                  education_start: this.education_start,
                }, {
                  headers: {
                    'EMAIL': global.this_email,
                    'AUTHORIZATION': global.this_token
                  }
                }).then(() =>{
                  that.$axios.post('people/upd_education_end', {
                    email: global.this_email,
                    id: this.id,
                    education_end: this.education_end,
                  }, {
                    headers: {
                      'EMAIL': global.this_email,
                      'AUTHORIZATION': global.this_token
                    }
                  }).then(() =>{
                    that.$axios.post('people/upd_education_experience', {
                      email: global.this_email,
                      id: this.id,
                      education_experience: this.education_experience,
                    }, {
                      headers: {
                        'EMAIL': global.this_email,
                        'AUTHORIZATION': global.this_token
                      }
                    }).then(() => {
                      that.check_finish()
                    })
                  })
                })
              })
            })
          })
        }
      }
    },
    check_delete() {
      // 向后端传递删除数据指令
      let that = this
      that.$axios.post('people/del_my_education_list', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then(() =>{
        that.check_finish()
      })
    }
  },
}
</script>

<style scoped>

.information_edit {
  background: rgba(248, 253, 253, 0.9);
  padding-left: 10px;
}

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

.check_box_3 {
  width: 90px;
  margin-right: 35px;
  margin-top: 10px;
  border: 1px solid gray;
  background: orangered;
  height: 32px;
  float: right;
}

</style>