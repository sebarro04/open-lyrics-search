import SignIn from './components/auth/SignIn';
import SignUp from './components/auth/SignUp';
import MainPage from './components/MainPage';
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
        <Route path='/mainPage' element={<MainPage />} />
      </Routes>
    </div>
    </BrowserRouter>
  )
}



export default App;