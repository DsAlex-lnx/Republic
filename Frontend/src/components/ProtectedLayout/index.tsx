import { useAuth } from '../../contexts/AuthProvider/useAuth'
import { Navigate } from 'react-router-dom'

export const ProtectedLayout = ({ children} : { children : JSX.Element | null }) => {

    const auth = useAuth()

    return auth?.username ? children : <Navigate to='/login' replace/>
}