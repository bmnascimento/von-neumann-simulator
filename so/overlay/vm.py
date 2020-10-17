#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

# CO: codigo de operacao
# OP: operando
# CI: contador de instrucoes
# AC: acumulador

# variáveis globais do sistema operacional
overlay_tree = {}

def main(code, debug):
    CI, AC, MEM, FILE = boot(code, debug)

    vezes = 0
    while True:
        if debug:
            if input('CI: {} AC: {}'.format(hex(CI), hex(AC))) == 'mem':
                range_inf = int(input('De '), 16)
                range_sup = int(input('Até '), 16)
                printMEM(MEM, range_inf, range_sup)
            print()

        CI, AC, status = executeInstruction(CI, AC, MEM, FILE, debug)

        if CI == 0x300 and True:
            vezes += 1
            print('\nVEZES:', vezes)
            for address, value in enumerate(MEM):
                if address % 64 == 0:
                    print(hex(address)[2:].zfill(3), ': ', end='')
                print(hex(value)[2:].zfill(2), end=' ')
                if address % 64 == 63:
                    print()
            if vezes >= 1:
                break

        if status == 'halt':
            print('Máquina parada')
            break

        elif status == 'error':
            print('Erro: Instrução desconhecida')
            break

def boot(code, debug):
    # carrega o código do loader na marra
    MEM = [0] * 0xf00
    MEM.extend([0xd0, 0x00, 0x9f, 0x44, 0x4f, 0x4b, 0x9f, 0x46, 0xd0, 0x00, 0x9f, 0x45, 0x9f, 0x47, 0xd0, 0x00, 0x9f, 0x4a, 0xd0, 0x00, 0x0f, 0x46, 0x8f, 0x47, 0x4f, 0x4c, 0x1f, 0x3a, 0x9f, 0x47, 0x8f, 0x4a, 0x5f, 0x4c, 0x9f, 0x4a, 0x1f, 0x28, 0x0f, 0x12, 0xd0, 0x00, 0x4f, 0x4b, 0x1f, 0x42, 0x9f, 0x46, 0xd0, 0x00, 0x9f, 0x47, 0xd0, 0x00, 0x9f, 0x4a, 0x0f, 0x12, 0x8f, 0x46, 0x4f, 0x4c, 0x9f, 0x46, 0x0f, 0x1c, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0f, 0x16, 0x00, 0x90, 0x01])
    MEM.extend([0] * 0xb3)

    AC = 0
    CI = 0xf00

    FILE = []
    for line in code.splitlines():
        for byte in line.split():
            FILE.append(int(byte, 16))

    return (CI, AC, MEM, FILE)


def executeInstruction(CI, AC, MEM, FILE, debug):
    global overlay_tree

    status = 'ok'

    CO = MEM[CI] >> 4
    OP = ((MEM[CI] % 0x10) << 8) + MEM[CI+1]

    if debug:
        print('CO: {} OP: {}'.format(hex(CO), hex(OP)))

    if CO == 0x0:  # JP
        CI = OP

    elif CO == 0x1: # JZ
        if AC == 0:
            CI = OP
        else:
            CI += 2

    elif CO == 0x2: # JN
        if AC < 0:
            CI = OP
        else:
            CI += 2

    elif CO == 0x3: # LV
        AC = OP
        CI += 2

    elif CO == 0x4: # +
        AC += MEM[OP]
        CI += 2

    elif CO == 0x5: # -
        AC -= MEM[OP]
        CI += 2

    elif CO == 0x6: # *
        AC *= MEM[OP]
        CI += 2

    elif CO == 0x7: # /
        AC = AC // MEM[OP]
        CI += 2

    elif CO == 0x8: # LD
        AC = MEM[OP]
        CI += 2

    elif CO == 0x9: # MM
        MEM[OP] = AC
        CI += 2

    elif CO == 0xa: # SC
        MEM[OP] = CI >> 8
        MEM[OP+1] = CI % 0x100
        CI = OP + 2

    elif CO == 0xb: # RS
        CI = OP

    elif CO == 0xc: # HM
        CI = OP
        status = 'halt'

    elif CO == 0xd: # GD
        if len(FILE) > 0:
            AC = FILE.pop(0)
        else:
            AC = 0x70
        CI += 2

    elif CO == 0xe: # PD
        #FILE.append(AC)
        print(hex(AC)[2:])
        CI += 2

    elif CO == 0xf: # OS
        if AC == 1: # configurar monitor de overlays
            # extrair o nome do arquivo
            config_file_name = ''
            pointer = OP
            ascii_char = MEM[pointer]
            while ascii_char != 0:
                config_file_name += chr(ascii_char)
                pointer += 1
                ascii_char = MEM[pointer]
            #print(config_file_name)

            # abrir o arquivo e montar estrutura da árvore
            overlay_tree = {}
            with open(config_file_name, 'r') as config_file:
                for line in config_file:
                    if not line.isspace():
                        contents = line.split()
                        if len(contents) > 3:
                            overlay_tree[int(contents[1])] = { 'filename': contents[2], 'depends on': int(contents[5]) }
                        else:
                            overlay_tree[int(contents[1])] = { 'filename': contents[2] }
            CI += 2
            #print(overlay_tree)

        elif AC == 2: # carrega overlay
            overlay = overlay_tree[MEM[OP]]

            # coloca overlay na fita para ser carregado pelo loader
            with open(overlay['filename'], 'r') as code_file:
                for line in code_file:
                    for byte in line.split():
                        FILE.append(int(byte, 16))

            # se tiver alguma dependência, colocar as dependências na lista
            while 'depends on' in overlay:
                overlay = overlay_tree[overlay['depends on']]
                with open(overlay['filename'], 'r') as code_file:
                    for line in code_file:
                        for byte in line.split():
                            FILE.append(int(byte, 16))

            # ir para o loader
            CI = 0xf00
    else:
        status = 'error'

    # overflow no acumulador
    return (CI, AC % 0x100, status)


def printMEM(MEM, range_inf, range_sup):
    for i in range(0, len(MEM), 16):
        if i >= range_inf and i <= range_sup:
            print('DEBUG MEM[{}]: '.format(hex(i)[2:].zfill(3)), end='')
            for j in range(0, 16):
                print(hex(MEM[i+j])[2:].zfill(2), end=' ')
            print()


with open(sys.argv[1], 'r') as hex_file:
    debug = '-d' in sys.argv
    main(hex_file.read(), debug)
