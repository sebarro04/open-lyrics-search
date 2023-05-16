import { onAuthStateChanged, signOut } from "firebase/auth";
import React, { useEffect, useState } from "react";
import { auth } from "../firebase/firebaseConfig";
import {useNavigate} from 'react-router-dom'

const MainPage = () => {
  const [authUser, setAuthUser] = useState(null);

  useEffect(() => {
    const listen = onAuthStateChanged(auth, (user) => {
      if (user) {
        setAuthUser(user);
      } else {
        setAuthUser(null);
      }
    });

    return () => {
      listen();
    };
  }, []);

  const userSignOut = () => {
    signOut(auth)
      .then(() => {
        console.log("sign out successful");
      })
      .catch((error) => console.log(error));
  };

  const navigate = useNavigate();

  return (
    <div>
      {authUser ? (
        <form className="containerLogOut">
          <p className="title">{`${authUser.email}`}</p>
          <button onClick={() => { userSignOut(); navigate('/'); }} className="buttonLogin">Cerrar Sesión</button>
        </form>
      ) : (
        <p></p>
      )}
    </div>
  );
};

export default MainPage;
