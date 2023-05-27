import React, { useEffect, useState } from "react";
import { signOut } from "firebase/auth";
import { auth } from "../firebase/firebaseConfig";
import { useNavigate } from "react-router-dom";

const DetailsPage = () => {
  const [data, setData] = useState([]);
  const navigate = useNavigate();

  const fetchData = () => {
    fetch("https://main-app.mangoocean-f33b36da.eastus.azurecontainerapps.io/open-lyrics-search/songs/6471c35b55b8c9931ee5b155")
      .then((response) => response.json())
      .then((jsonData) => {
        setData(jsonData[0]);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  };

  useEffect(() => {
    fetchData();
  }, []);

  const userSignOut = () => {
    signOut(auth)
      .then(() => {
        console.log("Sign out successful");
      })
      .catch((error) => console.log(error));
  };

  return (
    <div className="search_page-container">
      <div className="dataContainer">
        {/* Render the fetched data */}
        <div key={data._id}>{data.song_name}</div>
      </div>

      <form className="formContainer">
        <button onClick={() => navigate("/mainPage")} type="button" className="buttons">
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
