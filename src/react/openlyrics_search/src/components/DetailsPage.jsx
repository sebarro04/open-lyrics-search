import React, { useEffect, useState } from "react";
import { signOut } from "firebase/auth";
import { auth } from "../firebase/firebaseConfig";
import { useNavigate, useLocation } from "react-router-dom";

const DetailsPage = () => {
  const [songName, setSongName] = useState("");
  const [artistName, setArtistName] = useState("");
  const [genres, setGenres] = useState("");
  const [language, setLanguage] = useState("");
  const [popularity, setPopularity] = useState("");
  const [totalSongs, setTotalSongs] = useState("");
  const [lyrics, setLyrics] = useState("");
  const [id, setId] = useState("");
  const [song, setSong] = useState("");
  const navigate = useNavigate();
  const location = useLocation();

  const fetchData = () => {
    const link = "https://main-app.mangoocean-f33b36da.eastus.azurecontainerapps.io/open-lyrics-search/songs/";
    const combinedLink = `${link}${id}`;
    /*"https://main-app.mangoocean-f33b36da.eastus.azurecontainerapps.io/open-lyrics-search/songs/6471c35b55b8c9931ee5b155"*/
    fetch(combinedLink)
      .then((response) => response.json())
      .then((jsonData) => {
        setSongName(jsonData.song_name);
        setArtistName(jsonData.artist.name);
        setGenres(jsonData.artist.genres.join(", "));
        setLanguage(jsonData.language);
        setPopularity(jsonData.artist.popularity);
        setTotalSongs(jsonData.artist.songs);
        setLyrics(jsonData.lyric);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  };

  useEffect(() => {
    fetchData();
  }, );

  const userSignOut = () => {
    signOut(auth)
      .then(() => {
        console.log("Sign out successful");
      })
      .catch((error) => console.log(error));
  };

  useEffect(() => {
    if (location.state && location.state.filterNumber) {
      setId(location.state.filterNumber);
      setSong(location.state.song);
    }
  }, [location.state]);

  return (
    <div className="details_page-container">
      <form className="formDetails">
        <h1 className="titleDetails">{songName}</h1>
        <h3 className="textDetails">Nombre del artista: {artistName}</h3>
        <h3 className="textDetails">Géneros Musicales: {genres}</h3>
        <h3 className="textDetails">Idioma: {language}</h3>
        <h3 className="textDetails">Popularidad: {popularity}</h3>
        <h3 className="textDetails">Total de canciones del artista: {totalSongs}</h3>
        <h3 className="textDetails">Letra de la canción:</h3>
        <pre className="lyrics-text">{lyrics}</pre>
        <button onClick={() => navigate('/mainPage', { state: { song } })} type="button" className="buttons">
          Volver
        </button>
      </form>

      <form className="formLogOut">
        <button onClick={() => { userSignOut(); navigate("/"); }} className="buttons">
          Cerrar Sesión
        </button>
      </form>
    </div>
  );
};

export default DetailsPage;
