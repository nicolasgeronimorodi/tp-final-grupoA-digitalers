import React, {useState} from 'react'

const LinkForm=props=>{
    const [hayLink, setHayLink]=useState(false)
    const [enlaceOriginal, setEnlaceOriginal]=useState()



    const handleSubmit=e=>{
        e.preventDefault()
        localStorage.setItem('enlaceOriginal', enlaceOriginal)
      
        
    }


    return(
        
        <div>
            <h1> Ingresa el enlace que quieres acortar </h1>
            <form onSubmit={handleSubmit}> 
                <input
                type="text"
                onChange={e=> setHayLink(e.target.value)}
                className="input-text"
                />

                <input type="submit"
                value="Enviar"
                className="input-submit
                "
                />
            </form>
    
        </div>
    )
}
export default LinkForm