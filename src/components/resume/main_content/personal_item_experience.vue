<template>
  <div class="work_experience">
    <div style="padding-top: 15px" >
      <div style="float: left; height: 20px">
        <span class="iconfont icon-shuxian picture v_line"></span>
      </div>
      <span style="font-size: 18px; color: #414a60">项目经历</span>

      <span v-if="is_move_on" style="float: right; padding-right: 50px; font-size: 14px; font-weight: lighter; color: slategrey">编辑</span>
      <label v-if="is_move_on" class="iconfont icon-bianji" style="float: right; padding-right: 7px; padding-top: 1px"></label>

      <div @click="begin_new" style="float: right; cursor: pointer;padding-left: 20px;padding-right: 20px">
        <span style="float: right; padding-right: 10px; font-size: 14px; font-weight: lighter; color: slategrey">添加</span>
        <label class="iconfont icon-tianjia" style="float: right; padding-right: 7px; padding-top: 1px; cursor: pointer" ></label>
      </div>
    </div>

    <item_experience_edit_element v-if="new_id===-1" :is_new="true" @edit_finish_5="end_new" />

    <div v-for="id in id_list" style="padding-bottom: 20px;padding-right: 20px">
      <div class="element" :class="{po: move_on_id===id}" @mouseover="move_on(id)" @mouseout="move_out" >
        <item_experience_element v-if="!set_has(id)" :id="id" @click="edit(id)" />
        <item_experience_edit_element v-else :id="id" :is_new="false" @edit_finish_5="edit_finish(id)" />
      </div>
    </div>

  </div>
</template>

<script>
import item_experience_edit_element from "./experience/item_experience_edit_element.vue";
import item_experience_element from "./experience/item_experience_element.vue";
import {reactive} from "vue";
import global from "../../global.js";

export default {
  name: "personal_item_experience",
  setup () {
    let edit_set = new Set()
    const reactive_set = reactive(edit_set)

    function set_add(id) {
      reactive_set.add(id)
    }

    function set_delete(id) {
      reactive_set.delete(id)
    }

    function set_has(id) {
      return reactive_set.has(id)
    }

    function clear() {
      reactive_set.clear()
    }

    return {edit_set, set_add, set_delete, set_has, clear}
  },
  data() {
    return {
      new_id: -2, // -2代表未创建，-1代表创建
      id_list: [],
      move_on_id: -1
    }
  },
  beforeMount() {
    this.get_id_list()
    this.clear()
    this.move_on_id = -1
    this.new_id = -2
  },
  methods: {
    get_id_list() {
      // 从后端获取id_list
      let that = this
      that.$axios.post('people/get_my_item_list', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.id_list = res.data.my_item_list
      }).catch((res) => console.log(res))
    },
    get_id_list_edit(id) {
      // 从后端获取id_list
      let that = this
      that.$axios.post('people/get_my_item_list', {
        email: global.this_email
      }, {
        headers: {
          'EMAIL': global.this_email,
          'AUTHORIZATION': global.this_token
        }
      }).then((res) => {
        that.id_list = res.data.my_item_list
        that.set_delete(id)
      }).catch((res) => console.log(res))
    },
    move_on(id) {
      this.move_on_id = id
    },
    move_out() {
      this.move_on_id = -1
    },
    edit(id) {
      this.set_add(id)
    },
    edit_finish(id) {
      this.get_id_list_edit(id)  // 可能被删除或者创建，所以需要重新获取
      this.move_on_id = -1
      // this.set_delete(id)
    },
    begin_new() {
      this.new_id = -1
    },
    end_new() {
      this.get_id_list()  // 可能被创建，所以需要重新获取
      this.new_id = -2
    }
  },
  computed: {
    is_move_on() {
      return this.move_on_id !== -1
    },
  },
  components: [
    item_experience_edit_element,
    item_experience_element
  ]
}
</script>

<style scoped>

.work_experience {
  background: white;
  padding-left: 40px;
  padding-bottom: 20px;
}

.v_line {
  font-weight: bolder;
  font-size: 20px;
  color: #53cac3;
}

.po {
  cursor: pointer;
  background: white;
}

.element {
  /*width: 655px;*/
  border-radius: 5px;
}

</style>