import React, { useState, useEffect } from 'react'
import appStyle from './style/App.style'
import Code from './Code'
import Terminal from './Terminal'
import Memory from './Memory'

const App = () => {
  const [ newCode, setNewCode ] = useState('')

  useEffect(() => {
    console.log(newCode)
  })

  return (
    <>
      <header style={appStyle.header}>
        <h1 style={appStyle.title}>Simulador de Máquina de Von Neumann</h1>
      </header>
      <main style={appStyle.main}>
        <Code setNewCode={setNewCode}/>
        <Terminal />
        <Memory />
      </main>
    </>
  )
}

export default App
