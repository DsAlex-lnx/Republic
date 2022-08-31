import axios from 'axios'
import styles from './Register.module.css'
import React, { useState } from 'react'
import logo from '../../assets/logo.png'
import { Api } from '../../services/api'


export const Register = () => {
    
    const [name, setName] = useState('')
    const [phone, setPhone] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    async function handleRegister(e: React.FormEvent<HTMLInputElement>) {
        e.preventDefault()

        const data = {
            name,
            phone,
            email,
            password
        }

        try {
            const response = await Api.post('users/', data)
            alert('Ok')
        } catch (err) {
            alert('Not Ok')
        }
    }

    return (
        <div className={styles.main}>
            <div className={styles.container}>
                <div className={styles['sign-up']}>
                    <form onSubmit={ handleRegister }>
                        <div className={styles['logo-container']}>
                            <img src={ logo }></img>
                        </div>
                        <p>Use your email to registration</p>
                        <input type="text" name='name' placeholder='Name' value={name} onChange={e => setName(e.target.value)} required/>
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