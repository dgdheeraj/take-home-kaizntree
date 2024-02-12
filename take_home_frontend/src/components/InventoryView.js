import { React, useState, useContext, useEffect } from 'react';
import { useNavigate } from "react-router-dom";
import LoginContext from '../contexts/LoginContext';
import axios from 'axios';
import Cookies from 'js-cookie';

import 'bootstrap/dist/css/bootstrap.min.css';

function InventoryView(){
    const [items, setItems] = useState([]);

    const { login, changeLogin } = useContext(LoginContext);

    const navigate = useNavigate();

    // let logout = async (e) => {
    //     console.log(Cookies.get('sessionid'));
    // // axios.get("http://127.0.0.1:8000/api/v1/session/", {headers:{'X-CSRFToken':Cookies.get('csrftoken')}})
    // axios.get("http://127.0.0.1:8000/api/v1/session/",{withCredentials: true})
    //     .then(response => {
    //         console.log(response.data);
    //         if (response.status === 200) {
    //             console.log("Success")
    //             // changeLogin(false);
    //             // navigate("/inventory");
    //         } 
    //         else {
    //             // setError(response.data.detail);
    //             console.log(response.data);
    //         }
    //     })
    //     .catch(error => {
    //         console.error(error);
    //         // setError(error.response.data.detail)
    //     });
    // };
    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/v1/inventory/')
            .then(response => response.json())
            .then(data => {
                console.log(data);
                setItems([data])})
            .catch(error => console.error('Error fetching data:', error));
        }, []);
    

  return (
    <div >
        <div>
            <h3>Welcome to Item Dashboard</h3>
        </div>
        <br />
        {/* <button type="submit" className="btn btn-primary" onClick={logout}>logout</button> */}
    <table>
      <thead>
        <tr>
          <th>SKU</th>
          <th>Name</th>
          <th>Tags</th>
          <th>Category</th>
          <th>In Stock</th>
          <th>Available Stock</th>
        </tr>
      </thead>
      <tbody>
        {/* {items.map((item, index) => (
          <tr key={index}>
            <td>{item.sku}</td>
            <td>{item.name}</td>
            <td>{item.tags}</td>
            <td>{item.category}</td>
            <td>{item.in_stock}</td>
            <td>{item.available_stock}</td>
          </tr>
        ))} */}
      </tbody>
    </table>
    </div>
  );
};

export default InventoryView;