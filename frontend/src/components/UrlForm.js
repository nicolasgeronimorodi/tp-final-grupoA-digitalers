import React from 'react'

export default class UrlForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            url: null,
            alias: null,
            errors: {}
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.postUrl = this.postUrl.bind(this)
        this.handleValidation = this.handleValidation.bind(this)

    }

    handleValidation() {
        const expression = /((ftp|http|https):\/\/)?www\.([A-z]+)\.([A-z]{2,})/gi;
        let regex=new RegExp(expression)
        
        let errors = {};
        let formIsValid = true;
        if (!this.state.url) {
            formIsValid = false;
            errors["url"] = "No puede quedar vacío"
        }

        if (typeof this.state.url !== "undefined") {
            if (!this.state.url.match(regex)){ ///la regex tiene que incluir letras, numeros y obligatoriamente un punto
                formIsValid = false;
                errors["url"] = "Sólo letras"
            }
        }
        this.setState({ errors: errors });
        console.log('formIsValid' + formIsValid)
        return formIsValid

    }

    handleSubmit = (e) => {

        const payload = {
            url: this.state.url
        }
        e.preventDefault()
        if (this.handleValidation()) {
            alert("URL enviada");
            this.postUrl(payload)
            console.log(this.state.url)
        } else {
            alert("El formulario tiene errores")
        }
    }




    handleChange = (e) => {

        this.setState({ url: e.target.value })

    }

    postUrl = payload => {
        console.log("mandando payload")
        fetch('http://localhost:8000/api/',
            {
                method: 'POST',
                body: JSON.stringify(payload),
                headers: {
                    'Content-Type': 'application/json'
                }
            }
        ).then(response =>
            response.json()

        )
            .then(data => {
                console.log(data)
                console.log("el alias es" + data.alias)
                this.setState({ alias: data.alias })
            }
            )

    };

    handleRedirect=props=>{
        let alias=this.state.alias
        // props.history.push(alias)
    }


    render() {
        return (

            <>

                <section class="section">
                    <div class="columns">
                        <div class="column is-half-tablet is-one-quarter-fullhd">
                            <form onSubmit={this.handleSubmit}>
                                <p>Ingresar url</p>
                                <section class="section">
                                    <input class="input mb-5" type="text" placeholder="www.example.com" value={this.state.url} onChange={this.handleChange} />
                                    <button onClick={this.handleRedirect(this.props)}class="button is-primary">Acortar enlace</button>
                                </section>
                            </form>
                        </div>
                    </div>


                    <div class="response">
                        {this.state.alias}
                    </div>



                </section>
            </>
        )

    }
}

