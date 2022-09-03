import { useNavigate } from 'react-router-dom'
import styles from './Housing.module.css'
import React, { useState } from 'react'
import logo from '../../assets/logo.png'
import { Api } from '../../services/api'
import { getUserLocalStorage } from '../../contexts/AuthProvider/util'

export const HousingForm = () => {
    const navigate = useNavigate()

    const [title, setTitle] = useState('')
    const [description, setDescription] = useState('')
    const [price, setPrice] = useState('')
    const [house_type, setHouse_type] = useState('')
    const [street, setStreet] = useState('')
    const [district, setDistrict] = useState('')
    const [city, setCity] = useState('')
    const [zip_code, setZip_code] = useState('')
    const user_id = getUserLocalStorage().user_id

    const handleRegister = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault()

        const data = {
            title,
            description,
            price,
            house_type,
            address: {
                street,
                district,
                city,
                zip_code,
            }
        }

        try {
            const response = await Api.post('republics/', data)
            alert('Ok')
            navigate('/')
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
                        <input type="text" name='title' placeholder='Title' value={title} onChange={e => setTitle(e.target.value)} required/>
                        <input type="text" name='description' placeholder='Description' value={description} onChange={e => setDescription(e.target.value)} required/>
                        <input type='text' name='price' placeholder='Price' value={price} onChange={e => setPrice(e.target.value)} required/>
                        <input type='text' name='house_type' placeholder='1' value={house_type} onChange={e => setHouse_type(e.target.value)} required/>
                        <h3>Address Infos</h3>
                        <input type='text' name='street' placeholder='Street' value={street} onChange={e => setStreet(e.target.value)} required/>
                        <input type='text' name='district' placeholder='District' value={district} onChange={e => setDistrict(e.target.value)} required/>
                        <input type='text' name='city' placeholder='City' value={city} onChange={e => setCity(e.target.value)} required/>
                        <input type='text' name='zip_code' placeholder='Zip Code' value={zip_code} onChange={e => setZip_code(e.target.value)} required/>
                        <button type='submit'>Register</button>
                    </form>                
                </div>
            </div>
        </div>
    )
  }