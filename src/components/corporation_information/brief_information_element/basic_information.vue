<template>
  <div>
    <div style="margin-bottom: 30px">
      <div style="margin-bottom: 12px">
        <span style="font-size: 17px; font-weight: bolder">公司简介</span>
        <span v-if="move_on_1 && !is_check" style="float: right; padding-right: 50px; font-size: 16px; font-weight: lighter" >编辑</span>
        <label v-if="move_on_1 && !is_check" class="iconfont icon-bianji" style="font-size: 16px; float: right; padding-right: 7px; padding-top: 1px" ></label>
      </div>
      <div v-if="!edit_1 || is_check" :class="{edit_color: move_on_1&&!is_check, move_on: move_on_1&&!is_check}" style="padding: 5px" @mouseover="move_on_1=true" @mouseout="move_on_1=false" @click="click_edit_1">
        <div v-for="str in introduction_list">
          <span style="font-weight: 400; color: rgb(51, 51, 51); line-height: 28px">{{str}}</span>
          <br style="line-height: 28px">
        </div>
      </div>
      <div v-else>
        <el-input type="textarea" rows="15" v-model="edit_introduction" placeholder="请输入贵公司的公司简介" />
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
    </div>
    <div>
      <div>
        <span style="font-size: 17px; font-weight: bolder">人才发展</span>
        <div v-if="!is_check" style="float: right; cursor: pointer;padding-left: 20px;padding-right: 20px" @click="click_new">
          <span style="float: right; padding-right: 10px; font-size: 14px; font-weight: lighter; color: slategrey">添加</span>
          <label class="iconfont icon-tianjia" style="float: right; padding-right: 7px; padding-top: 1px; cursor: pointer" ></label>
        </div>
      </div>
      <div>
        <ul style="padding-left: 0">
          <li :class="{move_on: !is_check}" style="float: left; list-style-type: none; margin-right: 20px; margin-bottom: 6px; margin-top: 6px; padding: 3px 10px; border-radius: 4px; background: #f8f8f8" v-for="item in corporation_talent_development_list">
            <div style="" @click="click_edit_2(item)">
              <span style="font-size: 14px; color: #666666">{{item.content}}</span>
            </div>
          </li>
        </ul>
        <div style="clear:both;"></div>
      </div>
    </div>
    <el-dialog v-model="edit_2" width="40%" title="修改人才发展信息">
      <div>
        <el-input v-model="edit_talent_development" maxlength="10" placeholder="请输入贵公司人才发展信息" show-word-limit />
      </div>
      <div class="check">
        <div class="check_box_2" style="display: flex;align-items: center;text-align: center" @click="check_right_2(edit_id)">
          <label style="width: 90px; cursor: pointer">
            <span style="color: white">确定</span>
          </label>
        </div>
        <div class="check_box_1" style="display: flex;align-items: center;text-align: center" @click="check_finish_2">
          <label style="width: 90px; cursor: pointer">
            <span>取消</span>
          </label>
        </div>
        <div v-if="!is_new" class="check_box_3" style="display: flex;align-items: center;text-align: center" @click="check_delete_2(edit_id)">
          <label style="width: 90px; cursor: pointer">
            <span>删除</span>
          </label>
        </div>
      </div>
    </el-dialog>

    <el-dialog v-model="is_new" width="40%" title="添加人才发展信息">
      <div>
        <el-input v-model="edit_talent_development" maxlength="10" placeholder="请输入贵公司人才发展信息" show-word-limit />
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
import global from "../../global.js";

export default {
  name: "basic_information",
  props: ['is_check'],
  data() {
    return {
      corporation_introduction: "北京宏达盛丰科技有限公司致力于成为全球领先的专业IT产品、服务及解决方案供应商；为国内互联网企业、金融系统、通信企业、高科技领域、教育事业及能源领域提供资源外包和解决方案服务。 \n" +
          "\n" +
          "总部位于中国北京，目前宏达盛丰在北京、天津、广州、长沙、廊坊、桂林等城市设立分支机构\n" +
          "\n" +
          "公司经营范围包括产品、解决方案、行业应用、以及外包业务，拥有完全自主知识产权的OA、ERP、PLM软件产品。\n" +
          "\n" +
          "公司面向国内外客户提供优质的应用IT软件外包、信息服务及行业解决方案的供应商，在高科技、银行金融、移动通信、制造物流、保险、航信商旅、能源、烟草、医疗卫生、教育等行业积累了丰富的经验，具备专业的IT外包服务能力，为客户提供企业解决方案、应用软件开发、测试和运维、业务流程外包等服务，帮助客户实现收益最大化，并使之更专注于自身的核心业务。\n" +
          "\n" +
          "宏达盛丰致力于国内IT软件外包服务，能够为客户提供IT软件外包服务，并将IT外包（ITO）和业务流程外包（BPO） 有机的结合。拥有多个不同行业客户和技术领域服务能力，在交付方面拥有过硬的质量流程和专业领域知识保障，为客户提供优质外包服务。",
      corporation_talent_development_list: [
        {
          id: 1,
          content: "考核晋升"
        },
        {
          id: 2,
          content: "考核晋升"
        }
      ],

      edit_id: -1,
      edit_introduction: "",
      edit_talent_development: "",
      edit_record_item: "",

      move_on_1: false,
      move_on_2: false,
      edit_1: false,
      edit_2: false,
      new_2: false,
      is_new: false
    }
  },
  computed: {
    introduction_list() {
      let list = []
      let now_str = "";
      for (let c of this.corporation_introduction) {
        if (c !== '\n') {
          now_str = now_str + c
        }
        else {
          if (now_str !== "\n") {
            list.push(now_str)
            now_str = ""
          }
        }
      }
      list.push(now_str)
      return list
    }
  },
  mounted() {
    this.init_corporation_introduction()
    this.init_list()
  },
  methods: {
    init_corporation_introduction() {
      let that = this
      that.$axios.post('companies/get_corporation_introduction', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.corporation_introduction = res.data.corporation_introduction
      }).catch((res) => console.log(res))
    },
    init_list() {
      let that = this
      that.$axios.post('companies/get_corporation_talent_development_list', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.corporation_talent_development_list = res.data.corporation_talent_development_list
      }).catch((res) => console.log(res))
    },

    click_edit_1() {
      this.edit_1 = true
      this.edit_introduction = this.corporation_introduction
    },
    click_edit_2(list_name) {
      if (this.is_check) return
      this.edit_2 = true
      this.edit_id = list_name.id
      this.edit_record_item = list_name.content
      this.edit_talent_development = list_name.content
    },
    click_new() {
      this.is_new = true
      this.edit_talent_development = ""
    },
    check_finish() {
      this.edit_1 = false
    },
    check_right() {
      // 向后端传递修改（或新建）后的数据
      let that = this
      if (this.edit_introduction === "") {
        this.$message("请输入公司简介")
      } else {
        // 向后端传输
        that.$axios.post('companies/upd_corporation_introduction', {
          email: global.this_email,
          corporation_introduction: that.edit_introduction,
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then(() =>{
          that.init_corporation_introduction()
          this.check_finish()
        })
      }
    },
    check_finish_2() {
      this.edit_2 = false
      this.is_new = false
    },
    check_right_2(id) {
      // 向后端传递修改后的数据
      if (this.edit_talent_development === "") {
        this.$message("请不要修改为空")
      }
      else {
        let that = this
        that.$axios.post('companies/upd_corporation_talent_development', {
          email: global.this_email,
          id: id,
          content: that.edit_talent_development,
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then(() =>{
          that.init_list()
          this.check_finish_2()
        })
      }
    },
    check_delete_2(id) {
      // 向后端传递删除的数据
      // 向后端传输
      let that = this
      that.$axios.post('companies/del_corporation_talent_development_list', {
        email: global.this_email,
        id: id
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then(() =>{
        that.init_list()
        this.check_finish_2()
      })
    },
    check_new_2() {
      // 向后端传递新建后的数据
      if (this.edit_talent_development.length === 0) {
        this.$message("请不要修改为空")
      }
      else {
        // 向后端传输
        let that = this
        that.$axios.post('companies/add_corporation_talent_development_list', {
          email: global.this_email,
          content: that.edit_talent_development,
        }, {
          headers: {
            'EMAIL': global.this_email,
            'AUTHORIZATION': global.this_token
          }
        }).then(() =>{
          that.init_list()
          this.check_finish_2()
        })
      }
    }
  }
}
</script>

<style scoped>

.edit_color {
  background: #fafafa;
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