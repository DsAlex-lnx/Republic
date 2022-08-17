import axios from 'axios';
import { useEffect, useState } from 'react'
import { useQuery } from 'react-query'
import { Navbar } from './components/Nav/Navbar'

type Repository = {
  title: string;
  description: string;
}

function App() {

  return (
    <>
      <Navbar />
      <h1>Hello world</h1>
    </>
  )

  // const { data, isFetching, error } = useQuery<Repository[]>('republics', async () => {
  //   const response = await axios.get('https://127.0.0.1:8000/republics/')

  //   return response.data;
  // })

  // return (
  //   <ul>
  //     { isFetching && <p>Loading...</p> }
  //     { data?.map(repo => {
  //       return (
  //         <li key={repo.title}>
  //           <strong>{repo.title}</strong>
  //           <p>{repo.description}</p>
  //         </li>
  //       )
  //     })}
  //   </ul>
  // )
}

export default App
