import { createUserWithEmailAndPassword } from "firebase/auth";
import React, { useState } from "react";
import { auth } from "../../firebase/firebaseConfig";
import { collection, addDoc } from "firebase/firestore";
import db from '../../firebase/firebaseConfig';
import {useNavigate} from 'react-router-dom'

const SignUp = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");
  const [birthdate, setBirthdate] = useState("");

  const agregarDatos = async() => {        
    try {
      const docRef = await addDoc(collection(db, "user"), {
        email: email,
        profileName: name,
        birthdate: birthdate
      });
    
      console.log("Document written with ID: ", docRef.id);
    } catch (e) {
      console.error("Error adding document: ", e);
    }
  }

  const signUp = (e) => {
    e.preventDefault();
    createUserWithEmailAndPassword(auth, email, password)
      .then((userCredential) => {
        console.log(userCredential);
        agregarDatos();
        navigate('/mainPage')
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const navigate = useNavigate();

  return (
    <div className="sign-in_up-container">
      <form onSubmit={signUp} className="container">
        <h1 className="title">Crear Cuenta</h1>
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
        <h3 className="text">Ingrese su nombre de perfil</h3>
        <input
          className="textBox"
          type="text"
          placeholder="Nombre de perfil"
          value={name}
          onChange={(e) => setName(e.target.value)}
        ></input>
        <h3 className="text">Ingrese su fecha de nacimiento</h3>
        <input
          className="textBox"
          type="date"
          placeholder="Fecha de nacimiento"
          value={birthdate}
          onChange={(e) => setBirthdate(e.target.value)}
        ></input>
        <br></br>
        <button type="submit" className="buttonLogin">Registrarse</button>
        <button onClick={()=>navigate('/')} className="buttonLogin">Iniciar Sesión</button>
      </form>
    </div>
  );
};

export default SignUp;
