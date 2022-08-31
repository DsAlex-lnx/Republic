import React, { useState } from 'react'

import {
    BrowserRouter as Router,
    Route,
    Routes,
    Navigate,
} from 'react-router-dom'

import { Login } from './pages/login/Login'
import { Home } from './pages/homepage/Homepage'
import { Register } from './pages/register/Register'
import { AuthProvider } from './contexts/AuthProvider'
import { ProtectedLayout } from './components/ProtectedLayout'

const AppRoutes = () => {
    return (
        <Router>
            <AuthProvider>
                <Routes>
                    <Route path='/' element={<Home />} />
                    <Route path='login' element={<Login />} />
                    <Route path='register' element={<Register />} />
                    <Route path='user' element={(
                        <ProtectedLayout>
                            <Home />
                        </ProtectedLayout>
                    )}/>
                </Routes>
            </AuthProvider>
        </Router>
    )
}

export default AppRoutes