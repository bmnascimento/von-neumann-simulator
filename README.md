# Simulador de Máquina de Von Neumann

## Instruções

| Mnemônicos | Código | Instrução              |
|:----------:|:------:|:----------------------:|
| JP         | /0xxx  | Jump incondicional     |
| JZ         | /1xxx  | Jump if zero           |
| JN         | /2xxx  | Jump if negative       |
| LV         | /3xxx  | Load value             |
| +          | /4xxx  | Add                    |
| -          | /5xxx  | Subtract               |
| *          | /6xxx  | Multiply               |
| /          | /7xxx  | Divide                 |
| LD         | /8xxx  | Load from memory       |
| MM         | /9xxx  | Move to memory         |
| SC         | /Axxx  | Subroutine call        |
| RS         | /Bxxx  | Return from subroutine |
| HM         | /Cxxx  | Halt machine           |
| GD         | /Dxxx  | Get data               |
| PD         | /Exxx  | Put data               |
| OS         | /Fxxx  | Operating system call  |
| @          |        | Origin                 |
| #          |        | End                    |
| K          |        | Constant               |
