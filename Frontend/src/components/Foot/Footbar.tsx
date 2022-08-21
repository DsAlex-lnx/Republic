import React from 'react'
import styles from './Footbar.module.css'

export const Footbar: React.FC<{}> = () => {
    return (
        <footer className={styles.main}>
            <p>Devoloped by:</p>
            <strong>Alex Alves</strong>
        </footer>
    )}
