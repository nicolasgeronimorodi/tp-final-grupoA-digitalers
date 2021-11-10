import React, {useState, useEffect} from 'react'
const UrlFormFunctionBased=props=>{
    const [url, setUrl]=useState(undefined)
    const [alias, setAlias]=useState()

    const handleValidation=()=> {
        const expression = /((ftp|http|https):\/\/)?www\.([A-z]+)\.([A-z]{2,})/gi;
        let regex=new RegExp(expression)
        let errors = {};
        let formIsValid = true;
        if (!url) {
            formIsValid = false;
            errors["url"] = "No puede quedar vacío"
        }

        if (typeof url !== "undefined") {
            if (!url.match(regex)){ ///la regex tiene que incluir letras, numeros y obligatoriamente un punto
                formIsValid = false;
                errors["url"] = "Sólo letras"
            }
        }
        console.log('formIsValid' + formIsValid)
        return formIsValid

    }

    const handleSubmit = (e) => {

        const payload = {
            url: url
        }
        e.preventDefault()
        if (handleValidation()) {
            alert("URL enviada");
            postUrl(payload)
            console.log(url)
            props.history.push(`/alias/${alias}`)
            console.log(props.history)
        } else {
            alert("El formulario tiene errores")
        }
    }

    const handleChange = (e) => {
        setUrl(e.target.value)

    }

    
    const postUrl = payload => {
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
                console.log("el alias es " + data.alias)
                setAlias(data.alias)
            }
            )

    };

   


    return (
        <>
        <section class="section">
                    <div class="columns">
                        <div class="column is-half-tablet is-one-quarter-fullhd">
                            <form onSubmit={handleSubmit}>
                                <p>Ingresar url</p>
                                <section class="section">
                                    <input class="input mb-5" type="text" placeholder="www.example.com" 
                                    value={url || ""} 
                                    onChange={handleChange} 
                                    />
                                    <button class="button is-primary">Acortar enlace</button>
                                </section>
                            </form>
                        </div>
                    </div>


                    <div class="response">
                        {alias}
                    </div>
            </section>        


</>
)
}
export default UrlFormFunctionBased