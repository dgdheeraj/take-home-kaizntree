import { React, useState } from 'react';
import { useNavigate } from "react-router-dom";
import axios from 'axios';

function RegisterForm(){
    const [uname, setUname] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("")
    const [secondpassword, setSecondPassword] = useState("")
    const [error, setError] = useState("")

    const navigate = useNavigate();

    let handleSubmit = async (e) => {
    e.preventDefault();
    
    if (password !== secondpassword)
    {
        setError("Passwords don't match");
        return;
    }

    const data = {username: uname, password: password };
    axios.post("http://127.0.0.1:8000/api/v1/register/", data)
        .then(response => {
            console.log(response.data.detail);
            if (response.status === 200) {
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
            <h3>Register</h3>
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
                value={email}
                type="email"
                placeholder="Enter your email here"
                onChange={ev => setEmail(ev.target.value)}
                className="form-control" />
        </div>
        <div className={"form-group"}>
            <input
                value={password}
                type="password"
                id="password1"
                name="pwd1"
                placeholder="Enter your password here"
                onChange={ev => setPassword(ev.target.value)}
                className="form-control" />
        </div>
        <div className={"form-group"}>
            <input
                value={secondpassword}
                type="password"
                id="password2"
                name="pwd2"
                placeholder="Re enter your password here"
                onChange={ev => setSecondPassword(ev.target.value)}
                className="form-control" />
        </div>
        <button type="submit" className="btn btn-primary">Submit</button>
        </form>
        <br/>
        <div className={error?"alert alert-danger":""} role="alert">
        {error}
        </div>
    </div>
  );
};

export default RegisterForm;