import React from 'react'
import styles from './Navbar.module.css'
import logo from '../../assets/logo.png'
import * as data from './links.json'
import { useAuth } from '../../contexts/AuthProvider/useAuth'
import { Navigate, useNavigate } from 'react-router-dom'
import { Api } from '../../services/api'

const linksString = JSON.stringify(data)
const links = JSON.parse(linksString).links

type Link = {
    label: string;
    href: string;
};

const Links: React.FC<{ links: Link[] }> = ({ links }) => {
    return (
        <div className={styles['links-container']}>
            {links.map((link: Link ) => {
                return (
                    <div key={link.href} className={styles['links']}>
                        <a href={link.href}>
                            {link.label}
                        </a>
                    </div>
                    
                )
            })}
        </div>
    )
}

const Logout = async () => {
    const auth = useAuth()
    const navigate = useNavigate()
    try {
        const response = await Api.get('/logout')
        auth.logout()
        alert('You logged out!')
        navigate('/login')
    } catch (error){
        console.log(error)
    }

}

export const Navbar: React.FC<{}> = () => {
    return (
        <nav className={styles.navbar}>
            <div className={styles['logo-container']}>
                <img src={ logo }></img>
            </div>
            <button onClick={ Logout }>logout</button>
            <Links links={links} />
        </nav>
    )
}

