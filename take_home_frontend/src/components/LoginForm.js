import { React, useState, useContext } from 'react';
import { useNavigate } from "react-router-dom";
import LoginContext from '../contexts/LoginContext';
import axios from 'axios';

import 'bootstrap/dist/css/bootstrap.min.css';

function LoginForm(){
    const [uname, setUname] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const { login, changeLogin } = useContext(LoginContext);

    const navigate = useNavigate();

    let handleSubmit = async (e) => {
    e.preventDefault();

    const data = {username: uname, password: password };
    axios.post("http://127.0.0.1:8000/api/v1/login/", data)
        .then(response => {
            console.log(response.data.detail);
            if (response.status === 200) {
                changeLogin(true);
                navigate("/inventory");
            } 
            else {
                setError(response.data.detail);
            }
        })
        .catch(error => {
            setError(error.response.data.detail)
        });
    };

  return (
    <div >
        <div>
            <h3>Login</h3>
        </div>
        <br />
        
        <form onSubmit={handleSubmit}>
        <div className={"form-group"}>
            <input
                value={uname}
                placeholder="Enter your username here"
                onChange={ev => setUname(ev.target.value)}
                className="form-control" />
        </div>
        <div className={"form-group"}>
            <input
                type="password"
                value={password}
                placeholder="Enter your password here"
                onChange={ev => setPassword(ev.target.value)}
                className="form-control" />
        </div>
        <button type="submit" className="btn btn-primary">Submit</button>
        </form>
        <br/>
        <div className={error?"alert alert-danger":""} role="alert">
        {error}
        </div>
        <a href="/register">New User? Click here to register</a>
    </div>
  );
};

export default LoginForm;