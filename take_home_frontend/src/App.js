import logo from './logo.svg';
import './App.css';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';
import InventoryView from './components/InventoryView';
import {React} from 'react';
import {BrowserRouter as Router, Route, Routes, Navigate} from 'react-router-dom';

function App() {
  return (
    <div className="center">
        <Router basename={'/'}>
          <Routes>
            <Route index element={<Navigate to="/login" />} />
            <Route path="/login" element={<LoginForm/>}/>
            <Route path="/register" element={<RegisterForm/>}/>
            <Route path="/inventory" element={<InventoryView/>}/>
          </Routes>
        </Router>
    </div>
  );
}

export default App;
