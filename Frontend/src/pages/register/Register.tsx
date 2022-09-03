import { useNavigate } from 'react-router-dom'
import styles from './Register.module.css'
import React, { useState } from 'react'
import logo from '../../assets/logo.png'
import { Api } from '../../services/api'

export const Register = () => {
    const navigate = useNavigate()

    const [username, setUsername] = useState('')
    const [phone, setPhone] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    const handleRegister = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault()

        const data = {
            username,
            phone,
            email,
            password
        }

        try {
            const response = await Api.post('users/', data)
            alert('Ok')
            navigate('/login')
        } catch (error) {
            alert('Not Ok')
        }
    }

    return (
        <div className={styles.main}>
            <div className={styles.container}>
                <div className={styles['sign-up']}>
                    <form onSubmit={ handleRegister }>
                        <div className={styles['logo-container']}>
                           <a href='/'><img src={ logo }></img></a>
                        </div>
                        <p>Use your email to registration</p>
                        <input type="text" name='username' placeholder='Username' value={username} onChange={e => setUsername(e.target.value)} required/>
                        <input type="tex" name='phone' placeholder='Phone' value={phone} onChange={e => setPhone(e.target.value)} required/>
                        <input type='email' name='email' placeholder='Email' value={email} onChange={e => setEmail(e.target.value)} required/>
                        <input type='password' name='passwd' placeholder='Password' value={password} onChange={e => setPassword(e.target.value)} required/>
                        <button type='submit'>Register</button>
                    </form>                
                </div>
            </div>
        </div>
    )
  }