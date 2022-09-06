import React from 'react'
import axios from 'axios';
import styles from './Republic.module.css'
import { useQuery } from 'react-query'
import WhatsappPng from '../../assets/whatsapp.png'

type Repository = {
    title: string;
    description: string;
    price: number;
    username: string;
    phone: string;
    address: object;
    
}

export const Republic: React.FC<{}> = () => {
  const { data, isFetching } = useQuery<Repository[]>('republics', async () => {
    const response = await axios.get('https://127.0.0.1:8000/republics/')

    return response.data;
  })
  
  return (
    <div className={styles.main}>
        { isFetching && <p>Loading...</p> }
        { data?.map(republic => {
            return (
            <div className={styles['card-container']} key={ republic.title }>
                <strong>{ republic.title }</strong>
                <p>{ republic.description }</p>
                <p>Price: <strong>{ republic.price }.00</strong> || Owner: { republic.username }</p>
                <p>{ republic.address.street }, { republic.address.district }</p>
                <a href={`https://api.whatsapp.com/send/?phone=${republic.phone}`} target='_blank'>
                  <img className={styles['wpp-logo']} src={ WhatsappPng }>
                  </img>
                  <span className={styles['wpp-msg']}>Contact-me</span>
                </a>
                
            </div>
            )
        })}
    </div> 
  )
}