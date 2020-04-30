const executeInstruction = (CO, OP, CI, AC, MEM) => {
  // CO: código de operação
  // OP: operando
  // CI: contador de instruções
  // AC: acumulador
  // MEM: memória
  
  let HALT = false

  switch (OP) {
    case 0x0:  // JP
      CI = OP
      break
    case 0x1:  // JZ
      AC === 0 ? CI = OP : CI += 2
      break
    case 0x2:  // JN
      AC < 0 ? CI = OP : CI += 2
      break
    case 0x3:  // LV
      AC = OP
      CI += 2
      break
    case 0x4:  // +
      AC += MEM[OP]
      CI += 2
      break
    case 0x5:  // -
      AC -= MEM[OP]
      CI += 2
      break
    case 0x6:  // *
      AC *= MEM[OP]
      CI += 2
      break
    case 0x7:  // /
      AC /= MEM[OP]
      CI += 2
      break
    case 0x8:  // LD
      AC = MEM[OP]
      CI += 2
      break
    case 0x9:  // MM
      MEM[OP] = AC
      CI += 2
      break
    case 0xa:  // SC
      MEM[OP] = CI >> 8
      MEM[OP+1] = CI % 0x100
      CI = OP + 2
      break
    case 0xb:  // RS
      CI = OP
      break
    case 0xc:  // HM
      CI = OP
      HALT = true
      break
    case 0xd:  // GD
      // TODO implementar
      CI += 2
      break
    case 0xe:  // PD
      // TODO implementar
      CI += 2
      break
    case 0xf:  // OS
      // TODO implementar
      CI += 2
      switch (OP >> 8) {
        case 0x1:
          const valor = OP % 0x100
          console.log(valor.toString(16))
          break
      }
      break
    default:
      console.error('Instrução desconhecida')
  }

  return({ CI, AC, MEM, HALT })
}

export default vm
