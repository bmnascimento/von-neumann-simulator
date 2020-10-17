def run(code, infile):
    palavras = extrair(code)
    #print(palavras)
    
    Id = ''
    Num = 0
    Op = ''
    Comp1 = 0
    Comp2 = 0
    CompOp = ''
    isWrite = False
    outfile = ''
    inputs = infile.splitlines()

    variaveis = {}
    rotulos = {}
    state = 1

    i = 0
    while i < len(palavras):
        palavra = palavras[i]
        
        #print(variaveis)
        #print(rotulos)
        #print('state', state, 'palavra', palavra)

        if state == 1:
            if palavra == 'LET':
                state = 2
            elif palavra == 'READ':
                state = 6
            elif palavra == 'GOTO':
                state = 8
            elif palavra == 'WRITE':
                state = 4
                isWrite = True
            else:
                Id = palavra
                state = 14

        elif state == 2:
            Id = palavra
            state = 3
        
        elif state == 3:
            Op = '='
            state = 4
        
        elif state == 4:
            if palavra in variaveis:
                Num2 = variaveis[palavra]
            else:
                Num2 = int(palavra)

            if Op == '=':
                Num = Num2
            elif Op == '/':
                Num /= Num2
            elif Op == '*':
                Num *= Num2
            elif Op == '-':
                Num -= Num2
            elif Op == '+':
                Num += Num2
            state = 5
        
        elif state == 5:
            if palavra == '\n':
                if isWrite:
                    print(Num)
                    outfile += str(Num)
                else:
                    variaveis[Id] = Num
                state = 1
            else:
                Op = palavra
                state = 4
        
        elif state == 6:
            Id = palavra
            state = 7
        
        elif state == 7:
            variaveis[Id] = int(inputs.pop(0))
            state = 1
        
        elif state == 8:
            Id = palavra
            state = 9

        elif state == 9:
            if palavra == '\n':
                if Id in rotulos:
                    i = rotulos[Id]
                else:
                    for key, value in enumerate(palavras):
                        if (value == Id) and (palavras[key+1] == ':'):
                            i = key-1
                state = 1
            elif palavra == 'IF':
                Op = 'IF'
                state = 10

        elif state == 10:
            if palavra in variaveis:
                Num2 = variaveis[palavra]
            else:
                Num2 = int(palavra)

            if Op == 'IF':
                Num = Num2
            elif Op == '/':
                Num /= Num2
            elif Op == '*':
                Num *= Num2
            elif Op == '-':
                Num -= Num2
            elif Op == '+':
                Num += Num2
            state = 11
        
        elif state == 11:
            if palavra in ['>', '=', '<']:
                Comp1 = Num
                CompOp = palavra
                Op = CompOp
                state = 12
            else:
                Op = palavra
                state = 10
        
        elif state == 12:
            if palavra in variaveis:
                Num2 = variaveis[palavra]
            else:
                Num2 = int(palavra)

            if Op in ['>', '=', '<']:
                Num = Num2
            elif Op == '/':
                Num /= Num2
            elif Op == '*':
                Num *= Num2
            elif Op == '-':
                Num -= Num2
            elif Op == '+':
                Num += Num2
            state = 13
        
        elif state == 13:
            if palavra == '\n':
                Comp2 = Num
                if CompOp == '>':
                    if Comp1 > Comp2:
                        if Id in rotulos:
                            i = rotulos[Id]
                        else:
                            for key, value in enumerate(palavras):
                                if (value == Id) and (palavras[key+1] == ':'):
                                    i = key-1
                elif CompOp == '=':
                    if Comp1 == Comp2:
                        if Id in rotulos:
                            i = rotulos[Id]
                        else:
                            for key, value in enumerate(palavras):
                                if (value == Id) and (palavras[key+1] == ':'):
                                    i = key-1
                elif CompOp == '<':
                    if Comp1 < Comp2:
                        if Id in rotulos:
                            i = rotulos[Id]
                        else:
                            for key, value in enumerate(palavras):
                                if (value == Id) and (palavras[key+1] == ':'):
                                    i = key-1
                state = 1
            else:
                Op = palavra
                state = 12

        elif state == 14:
            rotulos[Id] = i
            state = 1
    
        i += 1

    return outfile


def extrair(code):
    code = code + '\n'
    palavras = []
    while len(code) > 0:
        nextChar = ''
        firstWord = ''
        while len(code) > 0:
            nextChar = code[0]
            code = code[1:]
            if nextChar in [':', '+', '-', '*', '/', ';', '=']:
                if firstWord != '':
                    palavras.append(firstWord)
                firstWord = nextChar
                palavras.append(firstWord)
                break
            elif nextChar == ' ':
                if firstWord != '':
                    palavras.append(firstWord)
                break
            elif nextChar == '\n':
                if firstWord != '':
                    palavras.append(firstWord)
                if (len(palavras) > 1) and (palavras[-1] != '\n'):
                    palavras.append(nextChar)
                break
            else:
                firstWord += nextChar
    
    return palavras


code = """
READ A
LOOP: LET A=A+1
GOTO LOOP IF A < 10
WRITE A
"""

#run(code, 'in.txt')