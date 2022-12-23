import { createApp } from 'vue'
import 'element-plus/dist/index.css'
import ElementPlus from 'element-plus'
import App from './App.vue'
import router from "./router/index.js";
import axiosInstance from "./axios/axios.js";
import '../font/1/iconfont.css'
import '../font/2/iconfont.css'
import '../font/3/iconfont.css'
import '../font/4/iconfont.css'
import '../font/5/iconfont.css'
import '../font/6/iconfont.css'
import '../font/7/iconfont.css'

const app = createApp(App)

app.use(router)
app.use(ElementPlus)
app.config.globalProperties.$axios = axiosInstance
app.config.globalProperties.$router = router

app.mount('#app')
