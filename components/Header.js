import React from "react"

const Header = () => {

  const headerStyle = {
    padding: "20px 0",
    lineHeight: "1.5em",
    backgroundColor: "#6B5B95",
    
}
  
  return (
    <header style={headerStyle}>
      <h1 style={{paddingLeft: "10px", fontSize: "6rem", fontWeight: "600", marginBottom: "2rem", lineHeight: "1em", color: "#eee", textTransform: "lowercase", textAlign: "left" }}>bitlyclone</h1>
    </header>
  )
}

export default Header