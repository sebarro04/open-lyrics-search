import { signOut } from "firebase/auth";
import React, { useState, useEffect } from "react";
import { auth } from "../firebase/firebaseConfig";
import { useNavigate, useLocation } from 'react-router-dom';

const MainPage = () => {
  const [song, setSong] = useState("");
  const [artist, setArtist] = useState("");
  const [language, setLanguage] = useState("");
  const [musicalGenre, setMusicalGenre] = useState("");
  const [maxPopularity, setMaxPopularity] = useState("");
  const [minPopularity, setMinPopularity] = useState("");
  const [maxTotalSongs, setMaxTotalSongs] = useState("");
  const [minTotalSongs, setMinTotalSongs] = useState("");

  const userSignOut = () => {
    signOut(auth)
      .then(() => {
        console.log("sign out successful");
      })
      .catch((error) => console.log(error));
  };

  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    if (location.state && location.state.song) {
      setSong(location.state.song);
    }
  }, [location.state]);

  const filters = () => {
    const formFacets = document.getElementById('facets');
    formFacets.style.display = formFacets.style.display === 'none' ? 'block' : 'none';
  }; 

  const listArtist = [
    { number: 100, label: "Aretha Franklin" },
    { number: 50, label: "Ray Charles" },
    { number: 30, label: "Elvis Presley" },
  ];

  const listLanguage = [
    { number: 100, label: "Inglés" },
    { number: 50, label: "Español" },
    { number: 30, label: "Francés" },
  ];

  const listMusicalGenre = [
    { number: 100, label: "Rock" },
    { number: 50, label: "Pop" },
    { number: 30, label: "Jazz" },
  ];

  const CheckboxChangeArtist = (value) => {
    if (artist.includes(value)) {
      // Remueve el valor si ya lo contiene
      setArtist(artist.filter((art) => art !== value));
    } else {
      // Agrega el valor si no lo contiene
      setArtist([...artist, value]);
    }
  };

  const CheckboxChangeLanguage = (value) => {
    if (language.includes(value)) {
      // Remueve el valor si ya lo contiene
      setLanguage(language.filter((lang) => lang !== value));
    } else {
      // Agrega el valor si no lo contiene
      setLanguage([...language, value]);
    }
  };

  const CheckboxChangeMusicalGenre = (value) => {
    if (musicalGenre.includes(value)) {
      // Remueve el valor si ya lo contiene
      setMusicalGenre(musicalGenre.filter((musGe) => musGe !== value));
    } else {
      // Agrega el valor si no lo contiene
      setMusicalGenre([...musicalGenre, value]);
    }
  };

  const [showOptionsArtist, setShowOptionsArtist] = useState(false);
  const [showOptionsLanguage, setShowOptionsLanguage] = useState(false);
  const [showOptionsMusicalGenre, setShowOptionsMusicalGenre] = useState(false);

  const ToggleOptionsArtist = () => {
    setShowOptionsArtist(!showOptionsArtist);
  };

  const ToggleOptionsLanguage = () => {
    setShowOptionsLanguage(!showOptionsLanguage);
  };

  const ToggleOptionsMusicalGenre = () => {
    setShowOptionsMusicalGenre(!showOptionsMusicalGenre);
  };

  return (
    <div className="main_page-container">
        <form  className="formSearch">
          <h3 className="text">OpenLyrics Search</h3>
          <input
            className="textBox"
            type="text"
            value={song}
            onChange={(e) => setSong(e.target.value)}
          ></input>
          <button onClick={() => { navigate('/detailsPage'); }} type="button" className="buttons">Buscar</button>

          <button type="button" className="buttons" onClick={filters}>Filtros</button>
        </form>
        
        <form id="facets" className="formFacets">
        <h3 className="filterText" onClick={ToggleOptionsArtist}>
            Nombre del Artista
          </h3>
          {showOptionsArtist && (
            <div>
              {listArtist.map((option) => (
                <div key={option.label} className="checkbox-option">
                  <label>
                    <input
                      className="checkbox"
                      type="checkbox"
                      value={option.label}
                      checked={artist.includes(option.label)}
                      onChange={(e) => CheckboxChangeArtist(e.target.value)}
                    />
                    <span className="option-content">
                      <span className="option-label">{option.label}</span>
                      <span className="number" style={{ float: 'right' }}>
                        {option.number}
                      </span>
                    </span>
                  </label>
                </div>
              ))}
            </div>
          )}

          <h3 className="filterText" onClick={ToggleOptionsLanguage}>
            Idioma
          </h3>
          {showOptionsLanguage && (
            <div>
              {listLanguage.map((option) => (
                <div key={option.label} className="checkbox-option">
                  <label>
                    <input
                      className="checkbox"
                      type="checkbox"
                      value={option.label}
                      checked={language.includes(option.label)}
                      onChange={(e) => CheckboxChangeLanguage(e.target.value)}
                    />
                    <span className="option-content">
                      <span className="option-label">{option.label}</span>
                      <span className="number" style={{ float: 'right' }}>
                        {option.number}
                      </span>
                    </span>
                  </label>
                </div>
              ))}
            </div>
          )}

          <h3 className="filterText" onClick={ToggleOptionsMusicalGenre}>
            Género Musical
          </h3>
          {showOptionsMusicalGenre && (
            <div>
              {listMusicalGenre.map((option) => (
                <div key={option.label} className="checkbox-option">
                  <label>
                    <input
                      className="checkbox"
                      type="checkbox"
                      value={option.label}
                      checked={musicalGenre.includes(option.label)}
                      onChange={(e) => CheckboxChangeMusicalGenre(e.target.value)}
                    />
                    <span className="option-content">
                      <span className="option-label">{option.label}</span>
                      <span className="number" style={{ float: 'right' }}>
                        {option.number}
                      </span>
                    </span>
                  </label>
                </div>
              ))}
            </div>
          )}

          <h3 className="text">Popularidad (0-5)</h3>
          <input
            className="textBox"
            type="text"
            placeholder="Máximo"
            value={maxPopularity}
            onChange={(e) => setMaxPopularity(e.target.value)}
          ></input>
          <input
            className="textBox"
            type="text"
            placeholder="Mínimo"
            value={minPopularity}
            onChange={(e) => setMinPopularity(e.target.value)}
          ></input>
          <h3 className="text">Total de canciones</h3>
          <input
            className="textBox"
            type="text"
            placeholder="Máximo"
            value={maxTotalSongs}
            onChange={(e) => setMaxTotalSongs(e.target.value)}
          ></input>
          <input
            className="textBox"
            type="text"
            placeholder="Mínimo"
            value={minTotalSongs}
            onChange={(e) => setMinTotalSongs(e.target.value)}
          ></input>
        </form>
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
