import { signOut } from "firebase/auth";
import React, { useState } from "react";
import { auth } from "../firebase/firebaseConfig";
import { useNavigate } from 'react-router-dom';

const SearchPage = () => {
  const [song, setSong] = useState("");
  const navigate = useNavigate();

  const userSignOut = () => {
    signOut(auth)
      .then(() => {
        console.log("sign out successful");
      })
      .catch((error) => console.log(error));
  };

  const handleSearch = () => {
    navigate('/mainPage', { state: { song } });
  };

  return (
    <div className="search_page-container">
      <form className="formContainer">
        <h1 className="title">OpenLyrics Search</h1>
        <input
          className="textBox"
          type="text"
          value={song}
          onChange={(e) => setSong(e.target.value)}
        />
        <button onClick={handleSearch} type="button" className="buttons">Buscar</button>
      </form>

      <form className="formLogOut">
        <button onClick={() => { userSignOut(); navigate('/'); }} className="buttons">Cerrar Sesión</button>
      </form>
    </div>
  );
};

export default SearchPage;
