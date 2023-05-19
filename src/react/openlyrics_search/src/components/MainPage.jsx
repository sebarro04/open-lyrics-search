import { signOut } from "firebase/auth";
import React, { useState } from "react";
import { auth } from "../firebase/firebaseConfig";
import {useNavigate} from 'react-router-dom'

const MainPage = () => {
  const [song, setSong] = useState("");
  const [name, setName] = useState("");
  const [language, setLanguage] = useState("");
  const [musicalGenre, setMusicalGenre] = useState("");
  const [popularity, setPopularity] = useState("");
  const [totalSongs, setTotalSongs] = useState("");

  const userSignOut = () => {
    signOut(auth)
      .then(() => {
        console.log("sign out successful");
      })
      .catch((error) => console.log(error));
  };

  const navigate = useNavigate();

  const songOptions = [
    { value: "default", label: "" },
    { value: "most", label: "Con más canciones primero" },
    { value: "least", label: "Con menos canciones primero" },
  ];

  const popularityOptions = [
    { value: "default", label: "" },
    { value: "most", label: "Más popular primero" },
    { value: "least", label: "Menos popular primero" },
  ];

  const filters = () => {
    const formFacets = document.getElementById('facets');
    formFacets.style.display = formFacets.style.display === 'none' ? 'block' : 'none';
  };  

  return (
    <div className="main_page-container">
      <div className="facets-container">
        <form  className="formContainer">
          <h3 className="text">Canción</h3>
          <input
            className="textBox"
            type="text"
            placeholder="Nombre de la canción"
            value={song}
            onChange={(e) => setSong(e.target.value)}
          ></input>
          <button type="button" className="buttons">Buscar</button>

          <button type="button" className="buttons" onClick={filters}>Filtros</button>
        </form>
        <form id="facets" className="formFacets">
          <h3 className="text">Nombre del artista</h3>
          <input
            className="textBox"
            type="text"
            placeholder="Nombre del artista"
            value={name}
            onChange={(e) => setName(e.target.value)}
          ></input>
          <h3 className="text">Idioma</h3>
          <input
            className="textBox"
            type="text"
            placeholder="Idioma"
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
          ></input>
          <h3 className="text">Género Musical</h3>
          <input
            className="textBox"
            type="text"
            placeholder="Género Musical"
            value={musicalGenre}
            onChange={(e) => setMusicalGenre(e.target.value)}
          ></input>
          <h3 className="text">Popularidad</h3>
          <select
            className="comboBox"
            value={popularity}
            onChange={(e) => setPopularity(e.target.value)}>
            {popularityOptions.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
          <h3 className="text">Total de canciones</h3>
          <select
            className="comboBox"
            value={totalSongs}
            onChange={(e) => setTotalSongs(e.target.value)}>
            {songOptions.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
        </form>
        </div>
      <form  className="formSongs">
        <h1 className="text">Resultados</h1>
      </form>
        <form className="formLogOut">
          <button onClick={() => { userSignOut(); navigate('/'); }} className="buttons">Cerrar Sesión</button>
        </form>
    </div>
  );
};

export default MainPage;
