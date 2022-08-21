import './App.css'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import { Home } from './pages/homepage/Homepage'
import { Login } from './pages/login/Login'
import { Register } from './pages/register/Register'

function App() {
  return (
    <Router>
      <Routes>
          <Route path='/' element={<Home />} />
          <Route path='login' element={<Login />} />
          <Route path='register' element={<Register />} />
      </Routes>
    </Router>
  )
}

export default App
