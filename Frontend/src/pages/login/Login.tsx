import { useNavigate } from 'react-router-dom'
import styles from './Login.module.css'
import logo from '../../assets/logo.png'
import React, { useState } from 'react'
import { useAuth } from '../../contexts/AuthProvider/useAuth'

export const Login = () => {
    const navigate = useNavigate()
    
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const auth = useAuth()

    const handleSubmit = async (e: React.FormEvent<HTMLChangeElement>) => {
        e.preventDefault();
        
        try {
            await auth.authenticate(username, password)
            navigate('/')
        } catch (error) {
            alert('Invalid Username or Password')
        }

    }

    return (
        <div className={styles.main}>
            <div className={styles.container}>
                <div className={styles['sign-in']}>
                    <form onSubmit={ handleSubmit }>
                        <div className={styles['logo-container']}>
                            <a href='/'><img src={ logo }></img></a>
                        </div>
                        <p>Use your username for sing in</p>
                        <input type='text' name='username' placeholder='Username' value={username} onChange={e => setUsername(e.target.value)} required/>
                        <input type='password' name='passwd' placeholder='Password' value={password} onChange={e => setPassword(e.target.value)} required/>
                        <a className={styles.fgt} href='#'>Forget your Password?</a>
                        <button type='submit'>Sign in</button>
                    </form>                
                </div>
                <p className={styles['register-txt']}>Dont have a account? <a href='/register'>Create Now</a></p>
            </div>
        </div>
    )
  }