import React, { Component } from 'react';
import { Admin, Resource } from 'react-admin';
//import jsonServerProvider from 'ra-data-json-server';
import logo from './logo.svg';
import './App.css';
import { PostList } from './posts';
import dataProvider from './dataProvider.js';


class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}


//const dataProvider = jsonServerProvider('http://jsonplaceholder.typicode.com');

//const dataProvider = jsonServerProvider('http://127.0.0.1:5000/api/v1/resources/kosmos/all');


const App1 = () => (
    <Admin dataProvider={dataProvider}>
        <Resource name="posts" list={PostList} />
    </Admin>
);


export default App1;
