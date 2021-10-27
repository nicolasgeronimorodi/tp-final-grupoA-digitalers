import React from 'react'
import HomePage from './HomePage';
import UrlForm from './UrlForm';

class App extends React.Component{
    constructor(props){
        super(props);
    }
render(){
    return( 
    <div>   
    <HomePage />
    <UrlForm />

    </div>
)
    }
}
export default App
