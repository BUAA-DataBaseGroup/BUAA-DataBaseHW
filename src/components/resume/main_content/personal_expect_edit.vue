<template>
  <div class="information_edit">
    <div style="padding-top: 20px; padding-bottom: 20px">
      <span style="color: #414a60; font-size: 16px">编辑求职期望</span>
    </div>
    <div class="information">

      <div class="line">
        <div class="first_row"  style="float: left">
          <div class="information_title">
            <span class="information_title_str">求职类型</span>
          </div>
          <div>
            <div class="type_box" :class="{type_selected: my_expect_work_type===1}" style="display: flex;align-items: center;text-align: center" @click="type_to_q">
              <label style="width: 147px; cursor: pointer">
                <span>全职</span>
              </label>
            </div>
            <div class="type_box" :class="{type_selected: my_expect_work_type===2}" style="display: flex;align-items: center;text-align: center" @click="type_to_j">
              <label style="width: 147px; cursor: pointer">
                <span>兼职</span>
              </label>
            </div>
          </div>
        </div>
        <div>
          <div class="information_title">
            <span class="information_title_str">工作城市</span>
          </div>
          <div style="width: 302px; float: left">
            <el-input v-model="my_expect_work_place" placeholder="请输入您的工作城市" maxlength="6" show-word-limit />
          </div>
        </div>
      </div>

      <div class="line">
        <div class="first_row"  style="float: left">
          <div class="information_title">
            <span class="information_title_str">期望职位</span>
          </div>
          <div style="width: 302px; float: left">
            <el-input v-model="my_expect_work_position" placeholder="请输入您的期望职位" maxlength="6" show-word-limit />
          </div>
        </div>
        <div>
          <div class="information_title">
            <span class="information_title_str">期望行业</span>
          </div>
          <div style="width: 302px; float: left">
            <el-input v-model="my_expect_work_field" placeholder="请输入您的期望行业" maxlength="10" show-word-limit />
          </div>
        </div>
      </div>

      <div v-if="my_expect_work_type === 1" class="line">
        <div class="first_row"  style="float: left">
          <div class="information_title">
            <span class="information_title_str">期望薪资</span>
          </div>
          <div style="width: 302px; float: left">
            <el-input-number v-if="my_expect_work_type===1" v-model="my_expect_salary" placeholder="请输入" :min="1" />
            <span style="font-size: 18px"> k</span>
          </div>
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
</template>

<script>
import global from "../../global.js";

export default {
  name: "personal_expect_edit",
  data() {
    return {
      my_expect_work_type: 0, // 0 -> 未选择，1 -> 全职，2 -> 兼职
      my_expect_work_place: "",
      my_expect_work_position: "",
      my_expect_work_field: "",
      my_expect_salary: 0,
      is_move_on: false
    }
  },
  mounted() {
    this.init_expect_work_type()
    this.init_expect_work_place()
    this.init_expect_work_position()
    this.init_expect_work_field()
    this.init_expect_salary()
  },
  methods: {
    init_expect_work_type() {
      let that = this
      that.$axios.post('people/get_my_expect_work_type', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_expect_work_type = res.data.my_expect_work_type
      }).catch((res) => console.log(res))
    },
    init_expect_work_place() {
      let that = this
      that.$axios.post('people/get_my_expect_work_place', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_expect_work_place = res.data.my_expect_work_place
      }).catch((res) => console.log(res))
    },
    init_expect_work_position() {
      let that = this
      that.$axios.post('people/get_my_expect_work_position', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_expect_work_position = res.data.my_expect_work_position
      }).catch((res) => console.log(res))
    },
    init_expect_work_field() {
      let that = this
      that.$axios.post('people/get_my_expect_work_field', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_expect_work_field = res.data.my_expect_work_field
      }).catch((res) => console.log(res))
    },
    init_expect_salary() {
      let that = this
      that.$axios.post('people/get_my_expect_salary', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_expect_salary = res.data.my_expect_salary
      }).catch((res) => console.log(res))
    },


    type_to_q() {
      this.my_expect_work_type = 1
    },
    type_to_j() {
      this.my_expect_work_type = 2
    },
    check_finish() {
      // 向前端输送完成编辑信号
      this.$emit("edit_finish_3")
    },
    check_right() {
      // 向后端传递修改后的数据
      if (this.my_expect_work_type === 0) {
        this.$message("请输入您的求职类型")
      }
      else if (this.my_expect_work_place === "") {
        this.$message("请输入您的期望工作城市")
      }
      else if (this.my_expect_work_position === "") {
        this.$message("请输入您的期望职位")
      }
      else if (this.my_expect_work_field === "") {
        this.$message("请输入您的期望行业")
      }
      else {
        let that = this
        that.$axios.post('people/upd_my_expect_work_place', {
          email: global.this_email,
          my_expect_work_place: that.my_expect_work_place
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then(() =>{
          that.$axios.post('people/upd_my_expect_work_position', {
            email: global.this_email,
            my_expect_work_position: that.my_expect_work_position
          }, {
            headers: {
              'EMAIL': global.this_email,
              'AUTHORIZATION': global.this_token
            }
          }).then(() =>{
            that.$axios.post('people/upd_my_expect_work_field', {
              email: global.this_email,
              my_expect_work_field: that.my_expect_work_field
            }, {
              headers: {
                'EMAIL': global.this_email,
                'AUTHORIZATION': global.this_token
              }
            }).then(() =>{
              that.$axios.post('people/upd_my_expect_work_type', {
                email: global.this_email,
                my_expect_work_type: that.my_expect_work_type
              }, {
                headers: {
                  'EMAIL': global.this_email,
                  'AUTHORIZATION': global.this_token
                }
              }).then(() =>{
                that.$axios.post('people/upd_my_expect_salary', {
                  email: global.this_email,
                  my_expect_salary: that.my_expect_salary
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

.type_box {
  width: 147px;
  margin-right: 16px;
  border: 1px solid gray;
  background: white;
  border-radius: 3px;
  height: 33px;
  float: left;
}

.type_selected {
  background: #dfdfdf;
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