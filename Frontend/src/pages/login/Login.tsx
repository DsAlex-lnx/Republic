import React from 'react'
import styles from './Login.module.css'
import logo from '../../assets/logo.png'

export const Login = () => {

    return (
        <div className={styles.main}>
            <div className={styles.container}>
                <div className={styles['sign-in']}>
                    <form action='#'>
                        <div className={styles['logo-container']}>
                            <img src={ logo }></img>
                        </div>
                        <p>Use your email for sing in</p>
                        <input type='email' name='email' placeholder='Email' required/>
                        <input type='password' name='passwd' placeholder='Password' required/>
                        <a className={styles.fgt} href='#'>Forget your Password?</a>
                        <button>Sign in</button>
                    </form>                
                </div>
                <p className={styles['register-txt']}>Dont have a account? <a href='/register'>Create Now</a></p>
            </div>
        </div>
    )
  }