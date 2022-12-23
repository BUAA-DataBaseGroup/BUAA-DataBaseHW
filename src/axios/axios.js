import axios from 'axios'

const axiosInstance = axios.create({
    baseURL: '/api',
    timeout: 2000,
    // headers: {
    //
    // }
})

export default axiosInstance