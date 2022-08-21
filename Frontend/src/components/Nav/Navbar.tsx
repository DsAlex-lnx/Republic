import React from 'react'
import styles from './Navbar.module.css'
import logo from '../../assets/logo.png'
import * as data from './links.json'

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

export const Navbar: React.FC<{}> = () => {
    return (
        <nav className={styles.navbar}>
            <div className={styles['logo-container']}>
                <img src={ logo }></img>
            </div>
            <Links links={links} />
        </nav>
    )
}

