# -*- coding: utf-8 -*-

import sys

tabela_mnemonicos = {
    'JP': 0x0,
    'JZ': 0x1,
    'JN': 0x2,
    'LV': 0x3,
    '+':  0x4,
    '-':  0x5,
    '*':  0x6,
    '/':  0x7,
    'LD': 0x8,
    'MM': 0x9,
    'SC': 0xA,
    'RS': 0xB,
    'HM': 0xC,
    'GD': 0xD,
    'PD': 0xE,
    'OS': 0xF
}

# remove espaços em branco e comentários
def make_listing(code):
    lines = code.splitlines()

    listing = ''
    for line in lines:
        line = line.strip()
        if line and not line.startswith(';'):
            listing += line.partition(';')[0] + '\n'

    return listing.upper()

def montador(code, com_checksum):
    listing = make_listing(code)
    # tabela de símbolos
    simbolos = {}

    print('DEBUG listing:')
    print(listing)

    # executa os dois passos da montagem
    for i in range(2):
        lines = listing.splitlines()

        object_code = ''
        size = 0
        checksum = 0

        for line in lines:
            line_elements = line.split()

            if len(line_elements) == 3:
                rotulo = line_elements.pop(0)
                simbolos[rotulo] = hex(current_line_address)[2:]

            mnemonico = line_elements[0]

            if len(line_elements) > 1:
                try:
                    operando = hex(int(line_elements[1], 16))[2:]
                except ValueError:
                    if line_elements[1] in simbolos:
                        operando = simbolos[line_elements[1]]
                    else:
                        operando = simbolos[line_elements[1]] = '000'
            else:
                operando = ''

            if mnemonico in tabela_mnemonicos:
                instrucao = hex(tabela_mnemonicos[mnemonico])[2:] + operando.zfill(3)
                object_code += instrucao
                print(hex(current_line_address) + ':', instrucao)
                current_line_address += 2
                size += 2
                checksum += int(instrucao[:2], 16) + int(instrucao[2:], 16)

            elif mnemonico == '@':
                if com_checksum:
                    size += 1
                    checksum += size
                    object_code += hex(((-checksum) % 0x100) & 0xff)[2:].zfill(2)

                object_code = object_code.replace('size', hex(size)[2:].zfill(2))

                current_line_address = int(line_elements[1], 16)
                endereco_inicial = hex(current_line_address)[2:].zfill(4)

                object_code += endereco_inicial
                #print(hex(current_line_address) + ':', hex(current_line_address)[2:].zfill(4))
                object_code += 'size'

                size = 0
                checksum = int(endereco_inicial[:2], 16) + int(endereco_inicial[2:], 16)

            elif mnemonico == '#':
                pass

            elif mnemonico == 'K':
                instrucao = operando.zfill(2)
                object_code += instrucao
                print(hex(current_line_address) + ':', instrucao)
                current_line_address += 1
                size += 1
                checksum += int(instrucao, 16)

    if com_checksum:
        size += 1
        checksum += size
        object_code += hex((~(checksum%0x100)+1) & 0xff)[2:].zfill(2)
        object_code = object_code[2:]

    object_code = object_code.replace('size', hex(size)[2:].zfill(2))

    print('DEBUG Tabela de símbolos:')
    for simbolo in simbolos:
        print(simbolo + ':', simbolos[simbolo])
    print()
    print('DEBUG Tabela código objeto:')

    output_code = ''
    for i in range(0, len(object_code), 32):
        for j in range(0, 32, 2):
            output_code += object_code[i+j:i+j+2] + ' '
            print(object_code[i+j:i+j+2], end=' ')
        output_code += '\n'
        print()

    return output_code

if '-c' in sys.argv:
    com_checksum = True
else:
    com_checksum = False

with open(sys.argv[1], 'r') as input_file:
    with open(sys.argv[2], 'w') as output_file:
        output_file.write(montador(input_file.read(), com_checksum))
