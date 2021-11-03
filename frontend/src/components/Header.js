import React from "react";




export default function Header() {
  return (
 
<>

<nav class="navbar is-dark" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
          <a class="navbar-item" href="https://bulma.io">
            <img
              src="https://bulma.io/images/bulma-logo.png"
              width="112"
              height="28"
            />
          </a>

          <a
            role="button"
            class="navbar-burger"
            aria-label="menu"
            aria-expanded="false"
            data-target="navbarBasicExample"
          >
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div id="navbarBasicExample" class="navbar-menu">
          

          <div class="navbar-end">
            <div class="navbar-item">
              <div class="buttons">
                
               
              </div>
            </div>
          </div>
        </div>
      </nav>
    <section class="section has-background-info">

      <div class="container">
        <h1 class="title">Acortador de Links</h1>
        <p class="subtitle"> Ahorrá espacio usando nuestra herramienta <strong></strong></p>
      </div>
    </section>
 

</>


  );
}
        