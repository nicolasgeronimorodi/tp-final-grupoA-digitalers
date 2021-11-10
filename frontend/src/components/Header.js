import React from "react";




export default function Header() {
  return (
<>

<nav className="navbar is-danger" role="navigation" aria-label="main navigation">
        <div className="navbar-brand">
          <a className="navbar-item" href="https://bulma.io">
            <img
              src="static/frontend/shorty-header-banner.png"
              width="112"
              height="28"
            />
          </a>
        </div>

        <div id="navbarBasicExample" className="navbar-menu">

          <div className="navbar-end">
            <div className="navbar-item">
              <div className="buttons">
              </div>
            </div>
          </div>
        </div>
      </nav>
    <section className="section has-background-black-ter">

      <div className="container">

        <h1 className="title has-text-grey-lighter">Acortador de Links</h1>
        <h2 className="subtitle has-text-grey-lighter"> Generá enlaces más cortos con esta herramienta </h2>

      </div>
    </section>

</>


  );
}