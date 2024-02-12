import './App.css';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';
import InventoryView from './components/InventoryView';
import LoginContext from './contexts/LoginContext';
import {React, useState } from 'react';
import {BrowserRouter as Router, Route, Routes, Navigate} from 'react-router-dom';

function App() {
  const [login, changeLogin] = useState(false);
  return (
    <LoginContext.Provider value={{ login: login, changeLogin: changeLogin }}>
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
    </LoginContext.Provider>
  );
}

export default App;
