<script>
import resume from "./components/resume.vue";
import corporation_information from "./components/corporation_information.vue";
import joblist from "./components/joblist.vue";
import job from "./components/job.vue"
import homepage_login from "./components/homepage_login.vue";
import homepage_unlogin from "./components/homepage_unlogin.vue";
import company_login from "./components/login_and_register/company_login.vue";
import employee_login from "./components/login_and_register/employee_login.vue";

export default {
  name: 'App',
  components: [
      resume,
      corporation_information,
      job,
      joblist,
      homepage_login,
      homepage_unlogin,
      company_login,
      employee_login
  ]
}
</script>

<template>
  <router-view  />
</template>

<style scoped>

</style>
