<template>
  <div class="resume_main_content">
    <div id="title_box">
      <span style="font-size: 14px; font-weight: bolder; color: #414a60">我的在线简历</span>
    </div>
    <div style="padding-top: 1px"></div>
    <div id="personal_resume_direction_one"></div>
    <personal_information v-if="!is_edit_1" :enter="is_move_on_1" class="information" :class="{move_on: is_move_on_1}" @mouseover="move_on_color_1" @mouseout="move_out_color_1" @click="click_1" />
    <personal_information_edit v-if="is_edit_1" @edit_finish_1="finish_1" />

    <div id="personal_resume_direction_two"></div>
    <personal_advantage v-if="!is_edit_2" :class="{move_on: is_move_on_2}" @mouseover="move_on_color_2" @mouseout="move_out_color_2" @click_2="click_2" />
    <personal_advantage_edit v-if="is_edit_2" @edit_finish_2="finish_2" />

    <div id="personal_resume_direction_three"></div>
    <personal_expect v-if="!is_edit_3" :class="{move_on: is_move_on_3}" @mouseover="move_on_color_3" @mouseout="move_out_color_3" @click_3="click_3" />
    <personal_expect_edit v-if="is_edit_3" @edit_finish_3="finish_3" />

    <div id="personal_resume_direction_four"></div>
    <personal_work_experience :class="{move_on: is_move_on_4}" @mouseover="move_on_color_4" @mouseout="move_out_color_4" />

    <div id="personal_resume_direction_five"></div>
    <personal_item_experience :class="{move_on: is_move_on_5}" @mouseover="move_on_color_5" @mouseout="move_out_color_5" />

    <div id="personal_resume_direction_six"></div>
    <personal_education_experience :class="{move_on: is_move_on_6}" @mouseover="move_on_color_6" @mouseout="move_out_color_6" />
  </div>
</template>

<script>
import personal_information_edit from "./main_content/personal_information_edit.vue";
import personal_information from "./main_content/personal_information.vue";
import personal_advantage from "./main_content/personal_advantage.vue";
import personal_advantage_edit from "./main_content/personal_advantage_edit.vue";
import personal_expect from "./main_content/personal_expect.vue";
import personal_expect_edit from "./main_content/personal_expect_edit.vue";
import personal_work_experience from "./main_content/personal_work_experience.vue";
import personal_item_experience from "./main_content/personal_item_experience.vue";
import personal_education_experience from "./main_content/personal_education_experience.vue";

export default {
  name: "resume_main_content",
  data() {
    return {
      is_move_on_1:false,
      is_edit_1: false,
      is_move_on_2: false,
      is_edit_2: false,
      is_move_on_3: false,
      is_edit_3: false,
      is_move_on_4: false,
      is_move_on_5: false,
      is_move_on_6: false
    }
  },
  methods: {
    move_on_color_1() {
      this.is_move_on_1 = true
    },
    move_out_color_1() {
      this.is_move_on_1 = false
    },
    click_1() {
      this.is_edit_1 = true
    },
    finish_1() {
      this.is_edit_1 = false
      this.is_move_on_1 = false
      // 从后端重新获取修改后的数据
    },
    move_on_color_2() {
      this.is_move_on_2 = true
    },
    move_out_color_2() {
      this.is_move_on_2 = false
    },
    click_2() {
      this.is_edit_2 = true
    },
    finish_2() {
      this.is_edit_2 = false
      this.is_move_on_2 = false
      // 从后端重新获取修改后的数据
    },
    move_on_color_3() {
      this.is_move_on_3 = true
    },
    move_out_color_3() {
      this.is_move_on_3 = false
    },
    click_3() {
      this.is_edit_3 = true
    },
    finish_3() {
      this.is_edit_3 = false
      this.is_move_on_3 = false
      // 从后端重新获取修改后的数据
    },
    move_on_color_4() {
      this.is_move_on_4 = true
    },
    move_out_color_4() {
      this.is_move_on_4 = false
    },
    move_on_color_5() {
      this.is_move_on_5 = true
    },
    move_out_color_5() {
      this.is_move_on_5 = false
    },
    move_on_color_6() {
      this.is_move_on_6 = true
    },
    move_out_color_6() {
      this.is_move_on_6 = false
    }
  },
  components: {
    personal_information,
    personal_information_edit,
    personal_advantage,
    personal_advantage_edit,
    personal_expect,
    personal_expect_edit,
    personal_work_experience,
    personal_item_experience,
    personal_education_experience
  }
}
</script>

<style scoped>

.resume_main_content {
  width: 730px;
}

#title_box {
  height: 40px;
  background: white;
  padding-left: 40px;

  display: flex;
  align-items: center;
}

.information {
  cursor: pointer;
}

.move_on {
  background: #f9f9f9;
}

</style>