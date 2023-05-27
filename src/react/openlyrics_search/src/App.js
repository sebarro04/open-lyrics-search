import SignUp from './components/auth/SignUp';
import SignIn from './components/auth/SignIn';
import SearchPage from './components/SearchPage';
import MainPage from './components/MainPage';
import DetailsPage from './components/DetailsPage';
import React from 'react'
import {BrowserRouter, Route, Routes} from 'react-router-dom'
import "./components/Design.css"

const App = () => {
  return (
    <BrowserRouter>
    <div className="App">
      <Routes>
        <Route path='/signUp' element={<SignUp />} />
        <Route path='/' element={<SignIn />} /> 
        <Route path='/searchPage' element={<SearchPage />} />
        <Route path='/mainPage' element={<MainPage />} />
        <Route path='/detailsPage' element={<DetailsPage />} />
      </Routes>
    </div>
    </BrowserRouter>
  )
}


export default App;