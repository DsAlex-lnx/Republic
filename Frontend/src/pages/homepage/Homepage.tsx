import React from 'react'
import { Navbar } from '../../components/Nav/Navbar'
import { Republic } from '../../components/Republic/Republic'
import { Footbar } from '../../components/Foot/Footbar'

export const Home = () => {

  return (
    <div className='App'>
      <Navbar />
      <Republic />
      <Footbar />
    </div>
  )
}
