#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

DEBUG = True

# instrucoes
JP = 0x0
JZ = 0x1
JN = 0x2
LV = 0x3
AD = 0x4 # +
SU = 0x5 # -
MU = 0x6 # *
DI = 0x7 # /
LD = 0x8
MM = 0x9
SC = 0xA
RS = 0xB
HM = 0xC
GD = 0xD
PD = 0xE
OS = 0xF

# memoria
CI = 0
AC = 0
MEM = [0] * 4096

# loader
with open(sys.argv[1], 'r') as file:
    code = ''.join(file.read().split())

    for i in range(0, len(code), 2):
        MEM[i//2] = int(code[i:i+2], 16)

        if DEBUG:
            print('DEBUG MEM[{0}]:'.format(hex(i//2)), hex(MEM[i//2]))

# CO: codigo de operacao
# OP: operando
# CI: contador de instrucoes
# AC: acumulador

while True:
    CO = MEM[CI] >> 4
    OP = ((MEM[CI] % 0x10) << 8) + MEM[CI+1]

    if DEBUG:
        print('DEBUG CO OP:', hex(CO), hex(OP))

    if CO == JP:
        CI = OP

    elif CO == JZ:
        if AC == 0:
            CI = OP
        else:
            CI += 2

    elif CO == JN:
        if AC < 0:
            CI = OP
        else:
            CI += 2

    elif CO == LV:
        AC = OP
        CI += 2

    elif CO == AD:
        AC += MEM[OP]
        CI += 2

    elif CO == SU:
        AC -= MEM[OP]
        CI += 2

    elif CO == MU:
        AC *= MEM[OP]
        CI += 2

    elif CO == DI:
        AC /= MEM[OP]
        CI += 2

    elif CO == LD:
        AC = MEM[OP]
        CI += 2

    elif CO == MM:
        MEM[OP] = AC
        CI += 2

    elif CO == SC:
        MEM[OP] = CI >> 8
        MEM[OP+1] = CI % 0x100
        CI = OP + 2

    elif CO == RS:
        CI = OP

    elif CO == HM:
        CI = OP
        break

    elif CO == GD:
        # TODO: implementar GD
        CI += 2

    elif CO == PD:
        # TODO: implementar PD
        CI += 2

    elif CO == OS:
        # TODO: implementar SO
        if (OP >> 8) == 0x1:
            print(hex(OP % 0x100))
        CI += 2

    else:
        print('Erro: Instrucao desconhecida')
        break
