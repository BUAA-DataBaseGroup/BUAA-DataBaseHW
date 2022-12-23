<template>
  <div id="resume_catalogue_box">
    <div class="parent" id="title">
      <h3 class="title_str">简历目录</h3>
    </div>
    <div onclick="window.open('#personal_resume_direction_one', '_self')" style="cursor:pointer;" class="item_of_catalogue parent" @mouseover="change_item_background(0)" @mouseleave="reset_item_background(0)" :style="{background: color[0]}" @click="emit_direction(1)">
      <span class="content_str">{{ catalogue[0] }}</span>
    </div>
    <div onclick="window.open('#personal_resume_direction_two', '_self')" style="cursor:pointer;" class="item_of_catalogue parent" @mouseover="change_item_background(1)" @mouseleave="reset_item_background(1)" :style="{background: color[1]}" @click="emit_direction(2)">
      <span class="content_str">{{ catalogue[1] }}</span>
    </div>
    <div onclick="window.open('#personal_resume_direction_three', '_self')" style="cursor:pointer;" class="item_of_catalogue parent" @mouseover="change_item_background(2)" @mouseleave="reset_item_background(2)" :style="{background: color[2]}" @click="emit_direction(3)">
      <span class="content_str">{{ catalogue[2] }}</span>
    </div>
    <div onclick="window.open('#personal_resume_direction_four', '_self')" style="cursor:pointer;" class="item_of_catalogue parent" @mouseover="change_item_background(3)" @mouseleave="reset_item_background(3)" :style="{background: color[3]}" @click="emit_direction(4)">
      <span class="content_str">{{ catalogue[3] }}</span>
    </div>
    <div onclick="window.open('#personal_resume_direction_five', '_self')" style="cursor:pointer;" class="item_of_catalogue parent" @mouseover="change_item_background(4)" @mouseleave="reset_item_background(4)" :style="{background: color[4]}" @click="emit_direction(5)">
      <span class="content_str">{{ catalogue[4] }}</span>
    </div>
    <div onclick="window.open('#personal_resume_direction_six', '_self')" style="cursor:pointer;" class="item_of_catalogue parent" @mouseover="change_item_background(5)" @mouseleave="reset_item_background(5)" :style="{background: color[5]}" @click="emit_direction(6)">
      <span class="content_str">{{ catalogue[5] }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "resume_catalogue",
  emits: ['direction'],
  data() {
    return {
      catalogue: [
          '个人信息',
          '个人优势',
          '期望职位',
          '工作经历',
          '项目经历',
          '教育经历'
      ],
      color: [
        'white',
        'white',
        'white',
        'white',
        'white',
        'white',
        'white'
      ]
    }
  },
  methods: {
    change_item_background(index) {
      this.color[index] = '#f0f0f0'
    },
    reset_item_background(index) {
      this.color[index] = 'white'
    },
    emit_direction(direction) {
      this.$emit('direction', direction)
      // console.log("direct to: " + direction)
    }
  }
}
</script>

<style scoped>
#resume_catalogue_box {
  width: 120px;
  /* 7*40+50 */
  height: 330px;
  background: white;
  border-radius: 5px;
  margin: 0;
}

#title {
  width: 120px;
  height: 50px;
  background: white;
}

.item_of_catalogue {
  width: 120px;
  height: 40px;
}

.parent {
  display: flex;
  align-items: center;
}

.content_str {
  color: #61687c;
  margin-left: 10px;
}

.title_str {
  font-weight: 500;
  margin-left: 10px;
  color: #24272e;
}

</style>