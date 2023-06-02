import { signOut } from "firebase/auth";
import React, { useState, useEffect } from "react";
import { auth } from "../firebase/firebaseConfig";
import { useNavigate, useLocation } from 'react-router-dom';

const MainPage = () => {
  const [song, setSong] = useState("");
  const [artist, setArtist] = useState("");
  const [language, setLanguage] = useState("");
  const [musicalGenre, setMusicalGenre] = useState("");
  const [popularity, setPopularity] = useState("");
  const [totalSongs, setTotalSongs] = useState("");

  const [listArtist, setListArtist] = useState([]);
  const [listLanguage, setListLanguage] = useState([]);
  const [listMusicalGenre, setListMusicalGenre] = useState([]);
  const [listPopularity, setListPopularity] = useState([]);
  const [listTotalSongs, setListTotalSongs] = useState([]);
  const [listSongs, setListSongs] = useState([]);

  const fetchData = () => {
    const link = "https://main-app.mangoocean-f33b36da.eastus.azurecontainerapps.io/open-lyrics-search/songs?search=";
    const search = encodeURIComponent(song);
    const combinedLink = `${link}${search}`;
    /*"https://main-app.mangoocean-f33b36da.eastus.azurecontainerapps.io/open-lyrics-search/songs?search=%22Love%22" */
    fetch(combinedLink)
      .then((response) => response.json())
      .then((jsonData) => {
        const names = jsonData.facets.facet.artist_name.buckets.map((bucket) => bucket._id);
        const artistSongs = jsonData.facets.facet.artist_name.buckets.map((bucket) => bucket.count);
        const updatedListArtist = names.map((name, index) => ({
          number: artistSongs[index],
          label: name,
        }));
        setListArtist(updatedListArtist);

        const languages = jsonData.facets.facet.language_facet.buckets.map((bucket) => bucket._id);
        const totalLanguages = jsonData.facets.facet.language_facet.buckets.map((bucket) => bucket.count);
        const updatedListLanguage = languages.map((name, index) => ({
          number: totalLanguages[index],
          label: name,
        }));
        setListLanguage(updatedListLanguage);

        const genres = jsonData.facets.facet.genres_facet.buckets.map((bucket) => bucket._id);
        const totalGenres = jsonData.facets.facet.genres_facet.buckets.map((bucket) => bucket.count);
        const updatedMusicalGenre = genres.map((name, index) => ({
          number: totalGenres[index],
          label: name,
        }));
        setListMusicalGenre(updatedMusicalGenre);

        const rating = jsonData.facets.facet.popularity_facet.buckets.map((bucket) => bucket._id);
        const totalRatingSongs = jsonData.facets.facet.popularity_facet.buckets.map((bucket) => bucket.count);
        const updatedPopularity = rating.map((name, index) => {
          if (name === "others" && index > 0) {
            return {
              number: totalRatingSongs[index],
              label: `Más de ${rating[index - 1]+49}`,
            };
          }
          return {
            number: totalRatingSongs[index],
            label: `${name}-${name+49}`,
          };
        });
        setListPopularity(updatedPopularity);

        const range = jsonData.facets.facet.songs_facet.buckets.map((bucket) => bucket._id);
        const totalSongsRange = jsonData.facets.facet.songs_facet.buckets.map((bucket) => bucket.count);
        const updatedTotalSongs = range.map((name, index) => {
          if (name === "others" && index > 0) {
            return {
              number: totalSongsRange[index],
              label: `Más de ${range[index - 1]+199}`,
            };
          }
          return {
            number: totalSongsRange[index],
            label: `${name}-${name+199}`,
          };
        });
        setListTotalSongs(updatedTotalSongs);

        const songsName = jsonData.songs.map((Song) => Song.song_name);
        const songsID = jsonData.songs.map((Song) => Song._id);
        const first100Songs = songsName.slice(0, 100);
        const first100ID = songsID.slice(0, 100);
        const updatedSongs = first100Songs.map((name, index) => ({
          label: name,
          number: first100ID[index],
        }));
        setListSongs(updatedSongs);
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

  const CheckboxChangePopularity = (value) => {
    if (popularity.includes(value)) {
      // Remueve el valor si ya lo contiene
      setPopularity(popularity.filter((po) => po !== value));
    } else {
      // Agrega el valor si no lo contiene
      setPopularity([...popularity, value]);
    }
  };

  const CheckboxChangeTotalSongs = (value) => {
    if (totalSongs.includes(value)) {
      // Remueve el valor si ya lo contiene
      setTotalSongs(totalSongs.filter((ts) => ts !== value));
    } else {
      // Agrega el valor si no lo contiene
      setTotalSongs([...totalSongs, value]);
    }
  };

  const [showOptionsArtist, setShowOptionsArtist] = useState(false);
  const [showOptionsLanguage, setShowOptionsLanguage] = useState(false);
  const [showOptionsMusicalGenre, setShowOptionsMusicalGenre] = useState(false);
  const [showOptionsPopularity, setShowOptionsPopularity] = useState(false);
  const [showOptionsTotalSongs, setShowOptionsTotalSongs] = useState(false);

  const ToggleOptionsArtist = () => {
    setShowOptionsArtist(!showOptionsArtist);
  };

  const ToggleOptionsLanguage = () => {
    setShowOptionsLanguage(!showOptionsLanguage);
  };

  const ToggleOptionsMusicalGenre = () => {
    setShowOptionsMusicalGenre(!showOptionsMusicalGenre);
  };

  const ToggleOptionsPopularity = () => {
    setShowOptionsPopularity(!showOptionsPopularity);
  };

  const ToggleOptionsTotalSongs = () => {
    setShowOptionsTotalSongs(!showOptionsTotalSongs);
  };

  const navigateToDetailsPage = (filterNumber) => {
    navigate('/detailsPage', { state: { song, filterNumber } });
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

          <h3 className="filterText" onClick={ToggleOptionsPopularity}>
            Popularidad
          </h3>
          {showOptionsPopularity && (
            <div>
              {listPopularity.map((option) => (
                <div key={option.label} className="checkbox-option">
                  <label>
                    <input
                      className="checkbox"
                      type="checkbox"
                      value={option.label}
                      checked={popularity.includes(option.label)}
                      onChange={(e) => CheckboxChangePopularity(e.target.value)}
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

          <h3 className="filterText" onClick={ToggleOptionsTotalSongs}>
            Total de canciones
          </h3>
          {showOptionsTotalSongs && (
            <div>
              {listTotalSongs.map((option) => (
                <div key={option.label} className="checkbox-option">
                  <label>
                    <input
                      className="checkbox"
                      type="checkbox"
                      value={option.label}
                      checked={totalSongs.includes(option.label)}
                      onChange={(e) => CheckboxChangeTotalSongs(e.target.value)}
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

        </form>
      <form  className="formSongs">
        <h1 className="text">Resultados</h1>
        <h3 className="text">
          {listSongs.map((cancion) => (
            <div
              className="filterText"
              onClick={() => navigateToDetailsPage(cancion.number)}
            >
              {cancion.label}
            </div>
          ))}
        </h3>
      </form>
        <form className="formLogOut">
          <button onClick={() => { userSignOut(); navigate('/'); }} className="buttons">Cerrar Sesión</button>
        </form>
    </div>
  );
};

export default MainPage;
