import React from 'react'

export default class UrlForm extends React.Component{
    constructor(props){
        super(props);
        this.state={
            url: null,
            apiResponse: null,
}
this.handleChange=this.handleChange.bind(this);
this.handleSubmit=this.handleSubmit.bind(this);

}
    
    handleSubmit=(e)=>{
        e.preventDefault()
        const payload={
            url: this.state.url
        }
        this.postUrl(payload)
        console.log(this.state.url)
        
    }

    handleChange=(e)=>{
        
        this.setState({url: e.target.value})

    }

postUrl=payload=>{
    console.log("mandando payload")
    await fetch('http://localhost:8000/api',
    {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: {
            'Content-Type': 'application/json'
        }
    }
    ).then(response=>response.json()    )
    .then(response=> console.log(response))
};
    render() {
        return( 
        
        <>
        
            <form onSubmit={this.handleSubmit}>
                <input type='text'
                value={this.state.url}
                onChange={this.handleChange}  />
            </form>
        
            
        </>
)        

}
}