import React, { useState } from 'react'

const Code = ({ setNewCode }) => {
  const codeStyle = {
    flex: 1, 
    display: 'flex',
    flexDirection: 'column',
  }

  const editorStyle = {
    display: 'block',
    resize: 'none',
    overflowX: 'auto',
    width: '95%',
    flex: 1,
    margin: 'auto',
    textAlign: 'left',
    padding: 5,
    backgroundColor: '#1e1e1e',
    color: '#d4d4d4',
    borderStyle: 'none',
    fontSize: '1.3em',
  }

  const buttonStyle = {
    margin: 10,
  }

  const [ code, setCode ] = useState('')

  const handleSimulate = () => {
    setNewCode(code)
  }

  return(
    <div style={codeStyle}>
      <textarea value={code} onChange={event => setCode(event.target.value)} style={editorStyle} wrap="off"/>
      <button onClick={handleSimulate} style={buttonStyle}>Simulate</button>
    </div>
  )
}

export default Code
