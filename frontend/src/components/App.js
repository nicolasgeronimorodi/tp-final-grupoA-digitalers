import React from 'react'
import Header from './Header';
import HomePage from './HomePage';
import UrlForm from './UrlForm';
import './App.css'

class App extends React.Component{
    constructor(props){
        super(props);
    }
render(){
    return( 
    <div className="wrapper">
    <Header />   
    <HomePage />
    <UrlForm />

    </div>
)
    }
}
export default App
