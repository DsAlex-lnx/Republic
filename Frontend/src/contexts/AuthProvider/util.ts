import { Api } from "../../services/api";
import { IUser } from "./types";

export const setUserLocalStorage = (user: IUser | null) => {
    localStorage.setItem('user', JSON.stringify(user))
}

export const getUserLocalStorage = () => {
    const json = localStorage.getItem('user')

    if (!json) {
        return null
    }

    const user = JSON.parse(json)

    return user ?? null 
}

export const LoginRequest = async (username: string, password: string) => {
    try {
        const request = await Api.post('login/', { username, password })
        
        return request.data
    } catch {
        return null;
    }
}