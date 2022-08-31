import axios from 'axios'
import { getUserLocalStorage } from '../contexts/AuthProvider/util'

export const Api = axios.create({
    baseURL: 'https://127.0.0.1:8000/',
})

Api.interceptors.request.use(
    (config) => {
        const user = getUserLocalStorage()

        config.headers!.Authorization = `Token ${user?.token}`

        return config
    }, 
    (error) => {
        return Promise.reject(error)
    }
)