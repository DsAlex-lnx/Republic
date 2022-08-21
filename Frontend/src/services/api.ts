import axios from 'axios'

export const Api = axios.create({
    baseURL: 'https://127.0.0.1:8000/',
})
