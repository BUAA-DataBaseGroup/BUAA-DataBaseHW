<template>
  <div class="information_edit">
    <div style="padding-top: 20px; padding-bottom: 20px">
      <span style="color: #414a60; font-size: 16px">编辑项目经历</span>
    </div>

    <div class="information">
      <div class="line">
        <div class="first_row" style="float: left">
          <div class="information_title">
            <span class="information_title_str">项目名称</span>
          </div>
          <div style="width: 302px">
            <el-input v-model="item_name" placeholder="请输入您的项目名称" maxlength="20" show-word-limit />
          </div>
        </div>
        <div style="float: left">
          <div class="information_title">
            <span class="information_title_str">项目角色</span>
          </div>
          <div style="width: 302px">
            <el-input v-model="item_role" placeholder="请输入您的项目角色" maxlength="10" show-word-limit />
          </div>
        </div>
      </div>

      <div class="line">
        <div style="float: left">
          <div class="information_title">
            <span class="information_title_str">项目链接（选填）</span>
          </div>
          <div style="width: 650px">
            <el-input v-model="item_link" placeholder="请输入您的项目链接" />
          </div>
        </div>
      </div>

      <div class="line">
        <div style="float: left">
          <div class="information_title">
            <span class="information_title_str">项目开始时间</span>
          </div>
          <div>
            <el-date-picker v-model="item_time" type="monthrange" value-format="YYYY-MM" range-separator="至" start-placeholder="开始时间" end-placeholder="结束时间" />
          </div>
        </div>
      </div>

      <div style="padding-bottom: 15px; width: 652px">
        <div class="information_title">
          <span class="information_title_str">项目描述</span>
        </div>
        <div>
          <el-input v-model="item_description" type="textarea" rows="7" resize="none" placeholder="请输入您的工作内容" maxlength="1500" show-word-limit />
        </div>
      </div>

      <div style="padding-bottom: 15px; width: 652px">
        <div class="information_title">
          <span class="information_title_str">项目业绩（选填）</span>
        </div>
        <div>
          <el-input v-model="item_achievement" type="textarea" rows="7" resize="none" placeholder="请输入您的工作业绩" maxlength="300" show-word-limit />
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
  name: "item_experience_edit_element",
  props: ['id', 'is_new'],
  emits: ['edit_finish_5'],
  data() {
    return {
      item_name: "",
      item_role: "",
      item_link: "",
      item_time: ["", ""],
      item_description: "",
      item_achievement: ""
    }
  },
  computed: {
    item_start() {
      return this.item_time.at(0)
    },
    item_end() {
      return this.item_time.at(1)
    }
  },
  mounted() {
    if (this.is_new) {
      this.item_name = ""
      this.item_role = ""
      this.item_link = ""
      this.item_time = ["", ""]
      this.item_description = ""
      this.item_achievement = ''
    }
    else {
      this.init_item_name()
      this.init_item_role()
      this.init_item_link()
      this.init_item_start()
      this.init_item_end()
      this.init_item_description()
      this.init_item_achievement()
    }
  },
  methods: {
    init_item_name() {
      let that = this
      that.$axios.post('people/get_item_name', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.item_name = res.data.item_name
      }).catch((res) => console.log(res))
    },
    init_item_role() {
      let that = this
      that.$axios.post('people/get_item_role', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.item_role = res.data.item_role
      }).catch((res) => console.log(res))
    },
    init_item_link() {
      let that = this
      that.$axios.post('people/get_item_link', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.item_link = res.data.item_link
      }).catch((res) => console.log(res))
    },
    init_item_start() {
      let that = this
      that.$axios.post('people/get_item_start', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.item_time[0] = res.data.item_start
      }).catch((res) => console.log(res))
    },
    init_item_end() {
      let that = this
      that.$axios.post('people/get_item_end', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.item_time[1] = res.data.item_end
      }).catch((res) => console.log(res))
    },
    init_item_description() {
      let that = this
      that.$axios.post('people/get_item_description', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.item_description = res.data.item_description
      }).catch((res) => console.log(res))
    },
    init_item_achievement() {
      let that = this
      that.$axios.post('people/get_item_achievement', {
        email: global.this_email,
        id: this.id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.item_achievement = res.data.item_achievement
      }).catch((res) => console.log(res))
    },

    check_finish() {
      // 向前端输送完成编辑信号
      this.$emit("edit_finish_5")
    },
    check_right() {
      // 向后端传递修改（或新建）后的数据
      if (this.item_name === "") {
        this.$message("请输入项目名称")
      }
      else if (this.item_role === "") {
        this.$message("请输入项目中您所处角色")
      }
      else if (this.item_time[0] === '' || this.item_time[1] === '') {
        this.$message("请输入项目时间")
      }
      else if (this.item_description === "") {
        this.$message("请输入项目描述")
      }
      else {
        let that = this
        if (this.is_new) {
          that.$axios.post('people/add_my_item_list', {
            email: global.this_email,
            item_name: this.item_name,
            item_role: this.item_role,
            item_link: this.item_link,
            item_start: this.item_start,
            item_end: this.item_end,
            item_description: this.item_description,
            item_achievement: this.item_achievement,
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
          that.$axios.post('people/upd_item_name', {
            email: global.this_email,
            id: this.id,
            item_name: this.item_name,
          }, {
            headers: {
              'EMAIL': global.this_email,
              'AUTHORIZATION': global.this_token
            }
          }).then(() =>{
            that.$axios.post('people/upd_item_role', {
              email: global.this_email,
              id: this.id,
              item_role: this.item_role,
            }, {
              headers: {
                'EMAIL': global.this_email,
                'AUTHORIZATION': global.this_token
              }
            }).then(() =>{
              that.$axios.post('people/upd_item_link', {
                email: global.this_email,
                id: this.id,
                item_link: this.item_link,
              }, {
                headers: {
                  'EMAIL': global.this_email,
                  'AUTHORIZATION': global.this_token
                }
              }).then(() =>{
                that.$axios.post('people/upd_item_start', {
                  email: global.this_email,
                  id: this.id,
                  item_start: this.item_start,
                }, {
                  headers: {
                    'EMAIL': global.this_email,
                    'AUTHORIZATION': global.this_token
                  }
                }).then(() =>{
                  that.$axios.post('people/upd_item_end', {
                    email: global.this_email,
                    id: this.id,
                    item_end: this.item_end,
                  }, {
                    headers: {
                      'EMAIL': global.this_email,
                      'AUTHORIZATION': global.this_token
                    }
                  }).then(() =>{
                    that.$axios.post('people/upd_item_description', {
                      email: global.this_email,
                      id: this.id,
                      item_description: this.item_description,
                    }, {
                      headers: {
                        'EMAIL': global.this_email,
                        'AUTHORIZATION': global.this_token
                      }
                    }).then(() => {
                      that.$axios.post('people/upd_item_achievement', {
                        email: global.this_email,
                        id: this.id,
                        item_achievement: this.item_achievement,
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
          })
        }
      }
    },
    check_delete() {
      // 向后端传递删除数据指令
      let that = this
      that.$axios.post('people/del_my_item_list', {
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