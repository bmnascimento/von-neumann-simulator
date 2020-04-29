import React from 'react'
import Code from './Code'
import Terminal from './Terminal'
import Memory from './Memory'

const App = () => {
  const headerStyle = {
    margin: 0,
    padding: "1em",
  }

  const titleStyle = {
    margin: 0,
  }

  const mainStyle = {
    display: "flex",
    justifyContent: "center",
    flexGrow: 1,
  }

  return (
    <>
      <header style={headerStyle}>
        <h1 style={titleStyle}>Von Neumann Simulator</h1>
      </header>
      <main style={mainStyle}>
        <Code />
        <Terminal />
        <Memory />
      </main>
    </>
  )
}

export default App
