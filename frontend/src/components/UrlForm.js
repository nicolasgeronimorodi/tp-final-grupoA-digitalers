import React from 'react'

export default class UrlForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            url: null,
            alias: null,
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.postUrl = this.postUrl.bind(this)

    }

    handleSubmit = (e) => {
        e.preventDefault()
        const payload = {
            url: this.state.url
        }
        this.postUrl(payload)
        console.log(this.state.url)


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



    render() {
        return (

            <>

                <section class="section">
                    <div class="columns">
                        <div class="column is-half-tablet is-one-quarter-fullhd">
                            <form onSubmit={this.handleSubmit}>
                                <p>Ingresar url</p>
                                <section class="section">
                                    <input class="input mb-5" type="text" placeholder="Text input" value={this.state.url} onChange={this.handleChange} />
                                    <button class="button is-primary">Acortar enlace</button>
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
