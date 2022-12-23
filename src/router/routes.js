import job from "../components/job.vue";
import homepage_unlogin from "../components/homepage_unlogin.vue";
import homepage_login from "../components/homepage_login.vue";
import joblist from "../components/joblist.vue";
import corporation_information from "../components/corporation_information.vue";
import resume from "../components/resume.vue";
import company_login from "../components/login_and_register/company_login.vue";
import employee_login from "../components/login_and_register/employee_login.vue";
import company_register from "../components/login_and_register/company_register.vue";
import employee_register from "../components/login_and_register/employee_register.vue";

const routes = [
    {
        name: 'homepage_unlogin',
        path: '/',
        component: homepage_unlogin
    },
    {
        name: 'homepage_login',
        path: '/homepage_login',
        component: homepage_login,
        props: true
    },
    {
        name: 'job',
        path: '/job/:email/:job_id/:re_id',
        component: job,
        props: true
    },
    {
        name: 'joblist',
        path: '/joblist/:search_str',
        component: joblist,
        props: true
    },
    {
        name: 'corporation_information_check',
        path: '/company/:company_email',
        component: corporation_information,
        props: true
    },
    {
        name: 'resume',
        path: '/resume',
        component: resume,
        props: true
    },
    {
        name: 'company_login',
        path: '/company_login',
        component: company_login
    },
    {
        name: 'employee_login',
        path: '/employee_login',
        component: employee_login
    },
    {
        name: 'company_register',
        path: '/company_register',
        component: company_register
    },
    {
        name: 'employee_register',
        path: '/employee_register',
        component: employee_register
    },

];

export default routes
