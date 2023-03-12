import React from 'react';
import ReactDOM  from 'react-dom';
//import * as serviceWorker from './serviceWorker';
import './index.css';
import { Routes, Route, BrowserRouter as Router } from 'react-router-dom';
import App from './App';
import Footer from './components/Footer';
import Header from './components/Header';

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <Router>
    <React.StrictMode>
      <Header/>
      <Routes>
        <Route exact path="/" component={App}></Route>
      </Routes>
      <Footer />
    </React.StrictMode>
  </Router>
);

