import React from 'react'
import axios from 'axios';
import styles from './Republic.module.css'
import { useQuery } from 'react-query'

type Repository = {
    title: string;
    description: string;
    price: number;
    user_name: string;
    user_phone: string;
    address_street: string;
    address_district: string;
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
                <p>Price: <strong>{ republic.price }.00</strong> || Owner: { republic.user_name }</p>
                <p>{ republic.address_street }, { republic.address_district }</p>
            </div>
            )
        })}
    </div> 
  )
}