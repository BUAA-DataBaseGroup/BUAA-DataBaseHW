<template>
  <div class="information_edit">
    <div class="title">
      <span id="title_str">编辑个人信息</span>
    </div>
    <div class="information">

      <div class="line">
        <div class="first_row" id="name">
          <div class="information_title">
            <span class="information_title_str">姓名</span>
          </div>
          <div>
            <input v-model="my_name" @blur="monitor_name" style="width: 302px; height: 30px">
          </div>
        </div>
        <div id="status">
          <div class="information_title">
            <span class="information_title_str">当前求职状态</span>
          </div>
          <div>
            <select v-model="my_status" style="width: 302px; height: 36px">
              <option value=0>离职-随时到岗</option>
              <option value=1>在职-暂不考虑</option>
              <option value=2>在职-考虑机会</option>
              <option value=3>在职-月内到岗</option>
            </select>
          </div>
        </div>
      </div>

      <div class="line">
        <div class="first_row" id="sex">
          <div class="information_title">
            <span class="information_title_str">性别</span>
          </div>
          <div>
            <div class="sex_box" :class="{sex_selected: my_sex_is_male}" style="display: flex;align-items: center;text-align: center" @click="sex_2_male">
              <label style="width: 147px; cursor: pointer">
                <span>男</span>
              </label>
            </div>
            <div class="sex_box" :class="{sex_selected: !my_sex_is_male}" style="display: flex;align-items: center;text-align: center" @click="sex_2_female">
              <label style="width: 147px; cursor: pointer">
                <span>女</span>
              </label>
            </div>
          </div>
        </div>
        <div id="date">
          <div class="information_title">
            <span class="information_title_str">生日</span>
          </div>
          <div>
            <el-date-picker v-model="my_birth" value-format="YYYY-MM-DD" :editable="false" :clearable="false" style="width: 302px; height: 36px" />
          </div>
        </div>
      </div>

      <div class="line">
        <div class="first_row" id="tel">
          <div class="information_title">
            <span class="information_title_str">电话</span>
          </div>
          <div>
            <input v-model="my_tel" @blur="monitor_tel" style="width: 302px; height: 30px">
          </div>
        </div>
        <div id="date_of_first_work">
          <div class="information_title">
            <span class="information_title_str">参加工作时间</span>
          </div>
          <div>
            <el-date-picker v-model="my_date_of_first_work" type="month" value-format="YYYY-MM" :editable="false" :clearable="false" style="width: 302px; height: 36px" />
          </div>
        </div>
      </div>

      <div class="line">
        <div class="first_row" id="wechat">
          <div class="information_title">
            <span class="information_title_str">微信号(选填)</span>
          </div>
          <div>
            <input v-model="my_wechat" @blur="monitor_wechat" placeholder="请输入您的微信号" style="width: 302px; height: 30px">
          </div>
        </div>
        <div id="email">
          <div class="information_title">
            <span class="information_title_str">邮箱（不可修改）</span>
          </div>
          <div>
            <input v-model="my_email" disabled style="width: 302px; height: 30px">
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
  name: "personal_information_edit",
  data() {
    return {
      // 点击“保存”后再将数据发回后端
      my_name: "",
      my_status: 2,
      my_sex_is_male: true,
      my_birth: "",
      my_tel: "",
      my_date_of_first_work: "",
      my_wechat: "",

      my_email: ""
    }
  },
  mounted() {
    this.my_email = global.this_email
    this.init_name()
    this.init_status()
    this.init_date_of_first_work()
    this.init_sex_is_male()
    this.init_wechat()
    this.init_birth()
    this.init_tel()
  },
  methods: {
    init_name() {
      let that = this
      that.$axios.post('people/get_my_name', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_name = res.data.my_name
      }).catch((res) => console.log(res))
    },
    init_status() {
      let that = this
      that.$axios.post('people/get_my_status', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_status = res.data.my_status
      }).catch((res) => console.log(res))
    },
    init_date_of_first_work() {
      let that = this
      that.$axios.post('people/get_my_date_of_first_work', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_date_of_first_work = res.data.my_date_of_first_work
      }).catch((res) => console.log(res))
    },
    init_sex_is_male() {
      let that = this
      that.$axios.post('people/get_my_sex_is_male', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_sex_is_male = res.data.my_sex_is_male
      }).catch((res) => console.log(res))
    },
    init_wechat() {
      let that = this
      that.$axios.post('people/get_my_wechat', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_wechat = res.data.my_wechat
      }).catch((res) => console.log(res))
    },
    init_birth() {
      let that = this
      that.$axios.post('people/get_my_birth', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_birth = res.data.my_birth
      }).catch((res) => console.log(res))
    },
    init_tel() {
      let that = this
      that.$axios.post('people/get_my_tel', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.my_tel = res.data.my_tel
      }).catch((res) => console.log(res))
    },
    monitor_name(event) {
      if (this.my_name !== event.target.value) {
        this.my_name = event.target.value
      }
    },
    sex_2_male() {
      if (this.my_sex_is_male !== true) {
        this.my_sex_is_male = true
      }
    },
    sex_2_female() {
      if (this.my_sex_is_male !== false) {
        this.my_sex_is_male = false
      }
    },
    monitor_tel(event) {
      if (this.my_tel !== event.target.value) {
        this.my_tel = event.target.value
      }
    },
    monitor_wechat(event) {
      if (this.my_wechat !== event.target.value) {
        this.my_wechat = event.target.value
      }
    },
    check_tel() {
      return this.my_tel.length === 11 && !isNaN(Number(this.my_tel));
    },
    check_finish() {
      // 向前端输送完成编辑信号
      this.$emit("edit_finish_1")
    },
    check_right() {
      // 向后端传递修改后的数据
      if (this.my_name === "") {
        this.$message("请输入您的姓名")
      }
      else if (this.my_status === -1) {
        this.$message("请输入您的当前求职状态")
      }
      else if (this.my_birth === "") {
        this.$message("请输入您的生日")
      }
      else if (this.my_tel === "") {
        this.$message("请输入您的电话")
      }
      else if(!this.check_tel()) {
        this.$message("请按正确格式输入电话")
      }
      else if (this.my_date_of_first_work === "") {
        this.$message("请输入您参加工作时间")
      }
      else {
        let that = this
        that.$axios.post('people/upd_my_name', {
          email: global.this_email,
          my_name: that.my_name
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then(() =>{
          that.$axios.post('people/upd_my_status', {
            email: global.this_email,
            my_status: that.my_status
          }, {
            headers: {
              'EMAIL': global.this_email,
              'AUTHORIZATION': global.this_token
            }
          }).then(() => {
            that.$axios.post('people/upd_my_birth', {
              email: global.this_email,
              my_birth: that.my_birth
            }, {
              headers: {
                'EMAIL': global.this_email,
                'AUTHORIZATION': global.this_token
              }
            }).then(() => {
              that.$axios.post('people/upd_my_tel', {
                email: global.this_email,
                my_tel: that.my_tel
              }, {
                headers: {
                  'EMAIL': global.this_email,
                  'AUTHORIZATION': global.this_token
                }
              }).then(() => {
                that.$axios.post('people/upd_my_date_of_first_work', {
                  email: global.this_email,
                  my_date_of_first_work: that.my_date_of_first_work
                }, {
                  headers: {
                    'EMAIL': global.this_email,
                    'AUTHORIZATION': global.this_token
                  }
                }).then(() => {
                  that.$axios.post('people/upd_my_wechat', {
                    email: global.this_email,
                    my_wechat: that.my_wechat
                  }, {
                    headers: {
                      'EMAIL': global.this_email,
                      'AUTHORIZATION': global.this_token
                    }
                  }).then(() => {
                    that.$axios.post('people/upd_my_sex_is_male', {
                      email: global.this_email,
                      my_sex_is_male: that.my_sex_is_male
                    }, {
                      headers: {
                        'EMAIL': global.this_email,
                        'AUTHORIZATION': global.this_token
                      }
                    }).then(() => that.check_finish())
                  })
                })
              })
            })
          })
        })
      }
    }
  }
}
</script>

<style scoped>

.information_edit {
  height: 440px;
  padding-left: 40px;

  background: rgba(248, 253, 253, 0.9);
}

.title {
  padding-top: 20px;
  padding-bottom: 15px;
}

#title_str {
  font-size: 18px;
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

.first_row {
  width: 350px;
}

#name {
  float: left;
}

/*#status {*/
/*  !*margin-left: 350px;*!*/
/*  float: left;*/
/*}*/

#sex {
  float: left;
}

.sex_box {
  width: 147px;
  margin-right: 16px;
  border: 1px solid gray;
  background: white;
  border-radius: 3px;
  height: 33px;
  float: left;
}

.sex_selected {
  background: #dfdfdf;
}

#tel {
  float: left;
}

#wechat {
  float: left;
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