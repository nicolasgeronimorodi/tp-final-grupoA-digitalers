import React from 'react'
import Header from './Header';
import HomePage from './HomePage';
import UrlForm from './UrlForm';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'
import UrlFormFunctionBased from './UrlFormFunctionBased';
import AliasPage from './AliasPage';
import './App.css'

class App extends React.Component{
    constructor(props){
        super(props);
    }
render(){
    return( 

    <div className="wrapper">
    <Header />   
    <HomePage cname="homepage"/>
    <Router>
    <Switch>
    <Route  exact path="/"  component={UrlFormFunctionBased} />
    <Route path="/alias/:alias" component={AliasPage} /> 
    </Switch>
    </Router>
    
    </div>
    )
    }
}
export default App
