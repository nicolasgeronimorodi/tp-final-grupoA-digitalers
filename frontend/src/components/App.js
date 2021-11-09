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
    <HomePage cname="homepage"/>
    <UrlForm />
    {/*<Router>
    <Switch>
    <Route  exact path="/"  component={UrlFormFunctionBased} />
    <Route path="/alias/:alias" component={AliasPage} /> 
    </Switch>
    </Router>*/}
    
    </div>
    )
    }
}
export default App
