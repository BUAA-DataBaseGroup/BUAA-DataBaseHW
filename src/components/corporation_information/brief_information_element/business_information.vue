<template>
  <div>
    <div style="margin-bottom: 30px">
      <div style="margin-bottom: 12px">
        <span style="font-size: 17px; font-weight: bolder">工商信息</span>
        <span v-if="move_on && !is_check" style="float: right; padding-right: 50px; font-size: 16px; font-weight: lighter" >编辑</span>
        <label v-if="move_on && !is_check" class="iconfont icon-bianji" style="font-size: 16px; float: right; padding-right: 7px; padding-top: 1px" ></label>
      </div>
      <div :class="{move_on: !is_check}" style="padding: 20px; border-radius: 10px; background: rgb(248, 248, 248)" @mouseover="move_on=true" @mouseout="move_on=false" @click="click_edit">
        <div>
          <div>
            <div style="width: 350px; padding-bottom: 30px; float: left; margin-right: 40px">
              <div class="information_title">
                <span class="information_title_str">企业名称：</span>
              </div>
              <div>
                <span class="str">{{corporation_name}}</span>
              </div>
            </div>
            <div v-if="corporation_LRP" style="width: 150px; float: left; padding-bottom: 30px; margin-right: 40px">
              <div class="information_title">
                <span class="information_title_str">法定责任人：</span>
              </div>
              <div>
                <span class="str">{{corporation_LRP}}</span>
              </div>
            </div>
            <div v-if="corporation_setup_time" style="width: 150px; float: left; padding-bottom: 30px">
              <div class="information_title">
                <span class="information_title_str">成立时间：</span>
              </div>
              <div>
                <span class="str">{{corporation_setup_time}}</span>
              </div>
            </div>
            <div style="clear:both;"></div>
          </div>
          <div>
            <div v-if="corporation_type!==-1" style="width: 350px; padding-bottom: 30px; float: left; margin-right: 40px">
              <div class="information_title">
                <span class="information_title_str">企业类型：</span>
              </div>
              <div>
                <span class="str">{{type_str(corporation_type)}}</span>
              </div>
            </div>
            <div v-if="corporation_status!==-1" style="width: 150px; float: left; padding-bottom: 30px; margin-right: 40px">
              <div class="information_title">
                <span class="information_title_str">经营状态：</span>
              </div>
              <div>
                <span class="str">{{status_str(corporation_status)}}</span>
              </div>
            </div>
            <div v-if="corporation_capital!==0" style="width: 150px; float: left; padding-bottom: 30px">
              <div class="information_title">
                <span class="information_title_str">注册资本：</span>
              </div>
              <div>
                <span class="str">{{corporation_capital}}万人民币</span>
              </div>
            </div>
            <div style="clear:both;"></div>
          </div>
          <div v-if="corporation_setup_place">
            <div style="padding-bottom: 30px">
              <div class="information_title">
                <span class="information_title_str">注册地址：</span>
              </div>
              <div>
                <span class="str">{{corporation_setup_place}}</span>
              </div>
            </div>
            <div style="clear:both;"></div>
          </div>
          <div v-if="corporation_SCC">
            <div style="padding-bottom: 30px">
              <div class="information_title">
                <span class="information_title_str">统一社会信用代码：</span>
              </div>
              <div>
                <span class="str">{{corporation_SCC}}</span>
              </div>
            </div>
            <div style="clear:both;"></div>
          </div>
          <div v-if="corporation_management_content">
            <div>
              <div class="information_title">
                <span class="information_title_str">经营范围：</span>
              </div>
              <div>
                <span class="str">{{corporation_management_content}}</span>
              </div>
            </div>
            <div style="clear:both;"></div>
          </div>
        </div>
      </div>
    </div>

    <el-dialog v-if="!is_check" v-model="edit" title="修改工商信息" width="65%">
      <div>
        <div>
          <div style="width: 350px; padding-bottom: 30px; float: left; margin-right: 40px">
            <div class="information_title">
              <span class="information_title_str">企业名称：</span>
            </div>
            <div>
              <el-input type="text" v-model="edit_name" placeholder="请输入您的企业名称" />
            </div>
          </div>
          <div style="width: 150px; float: left; padding-bottom: 30px; margin-right: 40px">
            <div class="information_title">
              <span class="information_title_str">法定责任人：</span>
            </div>
            <div>
              <el-input type="text" v-model="edit_LRP" placeholder="请输入法定责任人" />
            </div>
          </div>
          <div style="width: 150px; float: left; padding-bottom: 30px">
            <div class="information_title">
              <span class="information_title_str">成立时间：</span>
            </div>
            <div>
              <el-date-picker v-model="edit_setup_time" value-format="YYYY-MM" type="month" placeholder="请输入注册时间" />
            </div>
          </div>
          <div style="clear:both;"></div>
        </div>
        <div>
          <div style="width: 350px; padding-bottom: 30px; float: left; margin-right: 40px">
            <div class="information_title">
              <span class="information_title_str">企业类型：</span>
            </div>
            <div>
              <el-select v-model="edit_type" placeholder="请选择贵公司企业类型">
                <el-option :value="0" :label="type_str(0)" />
                <el-option :value="1" :label="type_str(1)" />
                <el-option :value="2" :label="type_str(2)" />
                <el-option :value="3" :label="type_str(3)" />
                <el-option :value="4" :label="type_str(4)" />
                <el-option :value="5" :label="type_str(5)" />
              </el-select>
            </div>
          </div>
          <div style="width: 150px; float: left; padding-bottom: 30px; margin-right: 40px">
            <div class="information_title">
              <span class="information_title_str">经营状态：</span>
            </div>
            <div>
              <el-select v-model="edit_status" placeholder="请选择经营状态">
                <el-option :value="0" :label="status_str(0)" />
                <el-option :value="1" :label="status_str(1)" />
                <el-option :value="2" :label="status_str(2)" />
                <el-option :value="3" :label="status_str(3)" />
                <el-option :value="4" :label="status_str(4)" />
                <el-option :value="5" :label="status_str(5)" />
                <el-option :value="6" :label="status_str(6)" />
                <el-option :value="7" :label="status_str(7)" />
              </el-select>
            </div>
          </div>
          <div style="width: 150px; float: left; padding-bottom: 30px">
            <div class="information_title">
              <span class="information_title_str">注册资本(万人民币)：</span>
            </div>
            <div>
              <el-input-number v-model="edit_capital" :min="3" />
            </div>
          </div>
          <div style="clear:both;"></div>
        </div>
        <div>
          <div style="padding-bottom: 30px">
            <div class="information_title">
              <span class="information_title_str">注册地址：</span>
            </div>
            <div>
              <el-input style="width: 80%" type="text" v-model="edit_setup_place" placeholder="请输入您的企业注册地址" />
            </div>
          </div>
          <div style="clear:both;"></div>
        </div>
        <div>
          <div style="padding-bottom: 30px">
            <div class="information_title">
              <span class="information_title_str">统一社会信用代码：</span>
            </div>
            <div>
              <el-input style="width: 80%" type="text" v-model="edit_SCC" show-word-limit maxlength="18" placeholder="请输入您的企业统一社会信用代码" />
            </div>
          </div>
          <div style="clear:both;"></div>
        </div>
        <div>
          <div>
            <div class="information_title">
              <span class="information_title_str">经营范围：</span>
            </div>
            <div>
              <el-input type="textarea" show-word-limit maxlength="1500" rows="8" v-model="edit_management_content" placeholder="请输入费贵公司的经营范围" />
            </div>
          </div>
          <div style="clear:both;"></div>
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
import global from "../../global.js";

export default {
  name: "business_information",
  props: ['is_check'],
  data() {
    return {
      corporation_abbreviation : "",

      corporation_name: "北京宏达盛丰科技有限公司",
      corporation_LRP: "秦桂东",
      corporation_setup_time: "2016-02-05",
      corporation_type: 3, //默认-1，0-5
      corporation_status: 6, //默认-1，0-7
      corporation_capital: 21, //默认0，最少3
      corporation_setup_place: "北京市海淀区丰慧中路7号新材料创业大厦10层10层南侧办公1966号",
      corporation_SCC: "91110116MA003JK61B",
      corporation_management_content: "一般项目：技术服务、技术开发、技术咨询、技术交流、技术转让、技术推广；对外承包工程；社会经济咨询服务；信息咨询服务（不含许可类信息咨询服务）；会议及展览服务；组织文化艺术交流活动；货物进出口；技术进出口；进出口代理；计算机软硬件及辅助设备批发；人工智能基础软件开发；软件开发；软件销售；软件外包服务；人工智能应用软件开发；数据处理服务。（除依法须经批准的项目外，凭营业执照依法自主开展经营活动）许可项目：职业中介活动。（依法须经批准的项目，经相关部门批准后方可开展经营活动，具体经营项目以相关部门批准文件或许可证件为准）（不得从事国家和本市产业政策禁止和限制类项目的经营活动。）",

      move_on: false,
      edit: false,

      edit_name: "",
      edit_LRP: "",
      edit_setup_time: "",
      edit_type: -1, //默认-1，0-5
      edit_status: -1, //默认-1，0-7
      edit_capital: 0, //默认0，最少3
      edit_setup_place: "",
      edit_SCC: "",
      edit_management_content: ""
    }
  },
  mounted() {
    this.init_corporation_name()
    this.init_corporation_corporation_LRP()
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
    init_corporation_corporation_LRP() {
      let that = this
      that.$axios.post('companies/get_corporation_LRP', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.corporation_LRP = res.data.corporation_LRP
        that.corporation_setup_time = res.data.corporation_setup_time
        that.corporation_type = res.data.corporation_type
        that.corporation_status = res.data.corporation_status
        that.corporation_capital = res.data.corporation_capital
        that.corporation_setup_place = res.data.corporation_setup_place
        that.corporation_SCC = res.data.corporation_SCC
        that.corporation_management_content = res.data.corporation_management_content

      }).catch((res) => console.log(res))
    },

    type_str(i) {
      switch (i) {
        case 0:
          return "国有企业"
        case 1:
          return "集体所有制"
        case 2:
          return "股份制企业"
        case 3:
          return "联营企业"
        case 4:
          return "个人独资企业"
        case 5:
          return "有限责任公司"
        default:
          return "error"
      }
    },
    status_str(i) {
      switch (i) {
        case 0:
          return "存续"
        case 1:
          return "在业"
        case 2:
          return "吊销"
        case 3:
          return "注销"
        case 4:
          return "迁入"
        case 5:
          return "迁出"
        case 6:
          return "停业"
        case 7:
          return "清算"
        default:
          return "error"
      }
    },
    click_edit() {
      this.edit = true
      this.edit_name = this.corporation_name
      this.edit_LRP = this.corporation_LRP
      this.edit_setup_time = this.corporation_setup_time
      this.edit_type = this.corporation_type === -1 ? "" : this.corporation_type
      this.edit_status = this.corporation_status === -1 ? "" : this.corporation_status
      this.edit_capital = this.corporation_capital === 0 ? 0 : this.corporation_capital
      this.edit_setup_place = this.corporation_setup_place
      this.edit_SCC = this.corporation_SCC
      this.edit_management_content = this.corporation_management_content
    },
    check_finish() {
      this.edit = false
    },
    check_right() {
      // 向后端传递修改（或新建）后的数据
      if (this.edit_name === "") {
        this.$message("请输入企业名称")
      }
      else if (this.edit_LRP === "") {
        this.$message("请输入企业法定责任人")
      }
      else if (this.edit_setup_time === "") {
        this.$message("请输入企业成立时间")
      }
      else if (this.edit_type === "") {
        this.$message("请输入企业类型")
      }
      else if (this.edit_status === "") {
        this.$message("请输入企业经营状态")
      }
      else if (this.edit_capital === "") {
        this.$message("请输入企业注册资金")
      }
      else if (this.edit_setup_place === "") {
        this.$message("请输入企业注册地址")
      }
      else if (this.edit_SCC === "") {
        this.$message("请输入企业统一社会信用代码")
      }
      else if (this.edit_management_content === "") {
        this.$message("请输入企业经营范围")
      }
      else {
        // 向后端输入
        let that = this
        that.$axios.post('companies/upd_corporation_name', {
          email: global.this_email,
          corporation_name: that.edit_name,
          corporation_abbreviation: that.corporation_abbreviation
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then(() =>{
          that.$axios.post('companies/upd_corporation_LRP', {
            email: global.this_email,
            corporation_LRP: that.edit_LRP,
            corporation_setup_time: that.edit_setup_time,
            corporation_type: that.edit_type,
            corporation_status: that.edit_status,
            corporation_capital: that.edit_capital,
            corporation_setup_place: that.edit_setup_place,
            corporation_SCC: that.edit_SCC,
            corporation_management_content: that.edit_management_content,
          }, {
            headers: {
              'EMAIL': global.this_email,
              'AUTHORIZATION': global.this_token
            }
          }).then(() =>{
            that.init_corporation_name()
            that.init_corporation_corporation_LRP()
            that.check_finish()
          })
        })
      }
    }
  }
}
</script>

<style scoped>

.information_title_str {
  font-size: 15px;
  color: #666666;
}

.information_title {
  padding-bottom: 3px;
}

.str {
  font-weight: lighter;
  font-size: 14px;
}

.check {
  height: 60px;
}

.check_box_1 {
  width: 90px;
  margin-right: 35px;
  margin-top: 20px;
  border: 1px solid gray;
  background: white;
  height: 32px;
  float: right;
}

.check_box_2 {
  width: 90px;
  margin-right: 50px;
  margin-top: 20px;
  border: 1px solid gray;
  background: #5dd5c8;
  height: 32px;
  float: right;
}

.move_on {
  cursor: pointer;
}

</style>