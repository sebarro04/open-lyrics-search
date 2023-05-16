import { signInWithEmailAndPassword } from "firebase/auth";
import React, { useState } from "react";
import { auth } from "../../firebase/firebaseConfig";
import {useNavigate} from 'react-router-dom'

const SignIn = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const signIn = (e) => {
    e.preventDefault();
    signInWithEmailAndPassword(auth, email, password)
      .then((userCredential) => {
        console.log(userCredential);
        navigate('/mainPage')
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const navigate = useNavigate();

  return (
    <div className="sign-in_up-container">
      <form onSubmit={signIn} className="container">
        <h1 className="title">Iniciar Sesión</h1>
        <h3 className="text">Ingrese su correo</h3>
        <input
          className="textBox"
          type="email"
          placeholder="Correo"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        ></input>
        <h3 className="text">Ingrese su contraseña</h3>
        <input
          className="textBox"
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        ></input>
        <br></br>
        <br></br>
        <button type="submit" className="buttonLogin">Iniciar Sesión</button>
        
        <button onClick={()=>navigate('/signUp')} className="buttonLogin">Registrarse</button>
      </form>
    </div>
  );
};

export default SignIn;
