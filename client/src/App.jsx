import React from 'react'
import { useState } from 'react'
import Home from './Components/Home'
import RegistrationForm from './Components/RegistrationForm'
import LoginForm from './Components/LoginForm'
import Navbar from './Components/Navbar'
import UserAccount from './Components/UserAccount'
import { Route, Routes } from 'react-router-dom'
import Footer from './Components/Footer'
import RestaurantMenu from './Components/RestaurantMenu'


 
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    
      <div>
     
        <Navbar />
      <Routes>
        <Route path='/' element={<Home />}></Route>
        <Route path='/register' element={<RegistrationForm />}></Route>
        <Route path='/login' element={<LoginForm />}></Route>
        <Route path='/account' element={<UserAccount/>}></Route>
        <Route path='/menu' element={<RestaurantMenu/>}></Route>
       

      </Routes>
      <Footer />
      
          
        </div>
       
       
    </>
  )
}

export default App
