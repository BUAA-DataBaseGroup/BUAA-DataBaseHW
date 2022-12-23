<template>
  <div>
    <div style="padding-left: 30px;padding-right: 30px; padding-top: 10px; background: white">
      <basic_information :is_check="is_check" style="margin-bottom: 30px" />
      <business_information :is_check="is_check" style="margin-bottom: 10px" />
    </div>
  </div>
</template>

<script>
import basic_information from "./brief_information_element/basic_information.vue";
import business_information from "./brief_information_element/business_information.vue";

export default {
  name: "brief_information",
  props: ['is_check'],
  components: [
    basic_information,
    business_information
  ]
}
</script>

<style scoped>

</style>