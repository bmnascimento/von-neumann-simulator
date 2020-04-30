import React, { useState } from 'react'

const MemoryField = ({ address, value, state }) => {
  const handleChange = event => {
    let MEMcopy = [ ...state.MEM ]
    MEMcopy[address] = event.target.value === '' ? 0 : parseInt(event.target.value, 16)
    state.setMEM(MEMcopy)
    console.log(MEMcopy)
  }

  return(
    <div>
      <label>{address.toString(16).toUpperCase()}</label>
      <input value={value.toString(16).toUpperCase()} onChange={handleChange} type="text"/>
    </div>
  )
}

const RegisterField = ({ label, value, set }) => {
  return(
    <div>
      <label>{label}</label>
      <input
        value={value.toString(16).toUpperCase()}
        onChange={event => event.target.value === '' ? 0 : set(parseInt(event.target.value, 16))}
        type="text"
      />
    </div>
  )
}

const Memory = () => {
  const memoryStyle = {
    flex: 1, 
    textAlign: 'right',
    padding: '0 1em',
  }

  const [ MEM, setMEM ] = useState(Array(4096).fill(0))
  const [ CI, setCI ] = useState(0)
  const [ AC, setAC ] = useState(0)

  return(
    <div style={memoryStyle}>
      <form>
        <RegisterField label="CI" value={CI} set={setCI}/>
        <RegisterField label="AC" value={AC} set={setAC}/>
        { MEM.map((value, address) => <MemoryField key={address} address={address} value={value} state={{ MEM, setMEM }}/>) }
      </form>
    </div>
  )
}

export default Memory
