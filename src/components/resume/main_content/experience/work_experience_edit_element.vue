<template>
  <div class="information_edit">
    <div style="padding-top: 20px; padding-bottom: 20px">
      <span style="color: #414a60; font-size: 16px">编辑工作经历</span>
    </div>

    <div class="information">
      <div class="line">
        <div class="first_row" style="float: left">
          <div class="information_title">
            <span class="information_title_str">公司名称</span>
          </div>
          <div style="width: 302px">
            <el-input v-model="company_name" placeholder="请输入您的工作单位" maxlength="20" show-word-limit />
          </div>
        </div>
        <div style="float: left">
          <div class="information_title">
            <span class="information_title_str">所属行业</span>
          </div>
          <div style="width: 302px">
            <el-input v-model="company_field" placeholder="请输入您的工作行业" maxlength="10" show-word-limit />
          </div>
        </div>
      </div>

      <div class="line">
        <div class="first_row" style="float: left">
          <div class="information_title">
            <span class="information_title_str">所属部门（选填）</span>
          </div>
          <div style="width: 302px">
            <el-input v-model="company_department" placeholder="请输入您的所属部门" maxlength="10" show-word-limit />
          </div>
        </div>
        <div style="float: left">
          <div class="information_title">
            <span class="information_title_str">职位名称</span>
          </div>
          <div style="width: 302px">
            <el-input v-model="company_position" placeholder="请输入您的职位名称" maxlength="6" show-word-limit />
          </div>
        </div>
      </div>

      <div class="line">
        <div class="first_row" style="float: left">
          <div class="information_title">
            <span class="information_title_str">在职时间</span>
          </div>
          <div style="width: 302px">
            <el-date-picker v-model="company_time" type="monthrange" value-format="YYYY-MM" range-separator="至" start-placeholder="开始时间" end-placeholder="结束时间" />
          </div>
        </div>
      </div>

      <div style="padding-bottom: 15px; width: 652px">
        <div class="information_title">
          <span class="information_title_str">工作内容</span>
        </div>
        <div>
          <el-input v-model="company_content" type="textarea" rows="7" resize="none" placeholder="请输入您的工作内容" maxlength="1500" show-word-limit />
        </div>
      </div>

      <div style="padding-bottom: 15px; width: 652px">
        <div class="information_title">
          <span class="information_title_str">工作业绩（选填）</span>
        </div>
        <div>
          <el-input v-model="company_achievement" type="textarea" rows="7" resize="none" placeholder="请输入您的工作业绩" maxlength="300" show-word-limit />
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
  name: "work_experience_edit_element",
  props: ['id', 'is_new'],
  emits: ['edit_finish_4'],
  data() {
    return {
      company_name: "",
      company_field: "",
      company_department: "",
      company_position: "",
      company_time: ["", ""],
      company_content: "",
      company_achievement: ""
    }
  },
  computed: {
    company_start() {
      return this.company_time.at(0)
    },
    company_end() {
      return this.company_time.at(1)
    }
  },
  mounted() {
    if (this.is_new) {
      this.company_name = ""
      this.company_field = ""
      this.company_department = ""
      this.company_position = ""
      this.company_time = ["", ""]
      this.company_content = ""
      this.company_achievement = ""
    }
    else {
      this.init_company_name()
      this.init_company_field()
      this.init_company_department()
      this.init_company_position()
      this.init_company_start()
      this.init_company_end()
      this.init_company_content()
      this.init_company_achievement()
    }
  },
  methods: {
    init_company_name() {
      let that = this
      that.$axios.post('people/get_company_name', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.company_name = res.data.company_name
      }).catch((res) => console.log(res))
    },
    init_company_field() {
      let that = this
      that.$axios.post('people/get_company_field', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.company_field = res.data.company_field
      }).catch((res) => console.log(res))
    },
    init_company_department() {
      let that = this
      that.$axios.post('people/get_company_department', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.company_department = res.data.company_department
      }).catch((res) => console.log(res))
    },
    init_company_position() {
      let that = this
      that.$axios.post('people/get_company_position', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.company_position = res.data.company_position
      }).catch((res) => console.log(res))
    },
    init_company_start() {
      let that = this
      that.$axios.post('people/get_company_start', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.company_time[0] = res.data.company_start
      }).catch((res) => console.log(res))
    },
    init_company_end() {
      let that = this
      that.$axios.post('people/get_company_end', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.company_time[1] = res.data.company_end
      }).catch((res) => console.log(res))
    },
    init_company_content() {
      let that = this
      that.$axios.post('people/get_company_content', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.company_content = res.data.company_content
      }).catch((res) => console.log(res))
    },
    init_company_achievement() {
      let that = this
      that.$axios.post('people/get_company_achievement', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.company_achievement = res.data.company_achievement
      }).catch((res) => console.log(res))
    },

    check_finish() {
      // 向前端输送完成编辑信号
      this.$emit("edit_finish_4")
    },
    check_right() {
      // 向后端传递修改（或新建）后的数据
      if (this.company_name === "") {
        this.$message("请输入公司名称")
      }
      else if (this.company_field === "") {
        this.$message("请输入公司所属行业")
      }
      else if (this.company_position === "") {
        this.$message("请输入职位名称")
      }
      else if (this.company_time.at(0) === "" || this.company_time.at(1) === "") {
        this.$message("请输入在职时间")
      }
      else if (this.company_content === "") {
        this.$message("请输入工作内容")
      }
      else {
        let that = this
        if (this.is_new) {
          that.$axios.post('people/add_my_work_list', {
            email: global.this_email,
            company_name: this.company_name,
            company_field: this.company_field,
            company_department: this.company_department,
            company_position: this.company_position,
            company_start: this.company_start,
            company_end: this.company_end,
            company_content: this.company_content,
            company_achievement: this.company_achievement,
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
          that.$axios.post('people/upd_company_name', {
            email: global.this_email,
            id: this.id,
            company_name: this.company_name,
          }, {
            headers: {
              'EMAIL': global.this_email,
              'AUTHORIZATION': global.this_token
            }
          }).then(() =>{
            that.$axios.post('people/upd_company_field', {
              email: global.this_email,
              id: this.id,
              company_field: this.company_field,
            }, {
              headers: {
                'EMAIL': global.this_email,
                'AUTHORIZATION': global.this_token
              }
            }).then(() =>{
              that.$axios.post('people/upd_company_department', {
                email: global.this_email,
                id: this.id,
                company_department: this.company_department,
              }, {
                headers: {
                  'EMAIL': global.this_email,
                  'AUTHORIZATION': global.this_token
                }
              }).then(() =>{
                that.$axios.post('people/upd_company_position', {
                  email: global.this_email,
                  id: this.id,
                  company_position: this.company_position,
                }, {
                  headers: {
                    'EMAIL': global.this_email,
                    'AUTHORIZATION': global.this_token
                  }
                }).then(() =>{
                  that.$axios.post('people/upd_company_start', {
                    email: global.this_email,
                    id: this.id,
                    company_start: this.company_start,
                  }, {
                    headers: {
                      'EMAIL': global.this_email,
                      'AUTHORIZATION': global.this_token
                    }
                  }).then(() =>{
                    that.$axios.post('people/upd_company_end', {
                      email: global.this_email,
                      id: this.id,
                      company_end: this.company_end,
                    }, {
                      headers: {
                        'EMAIL': global.this_email,
                        'AUTHORIZATION': global.this_token
                      }
                    }).then(() =>{
                      that.$axios.post('people/upd_company_content', {
                        email: global.this_email,
                        id: this.id,
                        company_content: this.company_content,
                      }, {
                        headers: {
                          'EMAIL': global.this_email,
                          'AUTHORIZATION': global.this_token
                        }
                      }).then(() =>{
                        that.$axios.post('people/upd_company_achievement', {
                          email: global.this_email,
                          id: this.id,
                          company_achievement: this.company_achievement,
                        }, {
                          headers: {
                            'EMAIL': global.this_email,
                            'AUTHORIZATION': global.this_token
                          }
                        }).then(() =>{
                          that.check_finish()
                        })
                      })
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
      that.$axios.post('people/del_my_work_list', {
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