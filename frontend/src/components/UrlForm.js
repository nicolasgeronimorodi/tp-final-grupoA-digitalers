import React from 'react';
import { CopyToClipboard } from 'react-copy-to-clipboard';

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
        const pattern = new RegExp('^(https?:\\/\\/)'+ // protocol
        '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // domain name
        '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
        '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
        '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
        '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
        let regex=new RegExp(pattern)
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
        let redirect_url = this.state.alias == null ? null : "http://localhost:8000/r/" + this.state.alias
        const url = redirect_url
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

                </section>
                                <section class="section">
                    <div class="columns">
                        <div class="column is-half-tablet is-one-quarter-fullhd">
                            {/*<a href= {redirect_url}>{redirect_url}</a><br/>*/}
                            <input class="input mb-5" type="text" placeholder="http://localhost:8000/r/AAAA111" value={redirect_url} onChange={this.handleChange} />
                            <button onClick={()=> window.open(redirect_url, "_blank")}class="button is-primary">Redireccionar</button>
                            <CopyToClipboard text={redirect_url}>
                                <button class="button is-primary">Copiar URL</button>
                            </CopyToClipboard>
                        </div>
                    </div>
                </section>
            </>
        )

    }
}

