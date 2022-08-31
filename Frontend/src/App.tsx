import './App.css'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import { Home } from './pages/homepage/Homepage'
import { Login } from './pages/login/Login'
import { Register } from './pages/register/Register'
import AppRoutes from './AppRoutes'

function App() {
  return (
    <div>
      <AppRoutes />
    </div>
  )
    
}

export default App
