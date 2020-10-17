# -*- coding: utf-8 -*-

global status
status = 'inicio'

def main():
    while True:
        if status in ['inicio', 'finalizar']:
            p0()
        elif status in ['iniciar']:
            p1()
        elif status in ['caractere']:
            p2()
        elif status in ['sequencia delimitada']:
            p3()
        elif status in ['sequencia alfabetica']:
            p4()
        elif status in ['tabela de referencias cruzadas']:
            p5()
        elif status in ['linha numerada', 'linha a imprimir']:
            p6()
        elif status in ['fim']:
            break

def p0():
    global status
    global referencias
    global ocorrencias
    global numero_da_linha
    global caractere
    global texto
    global primeiro_caractere
    global alfabetico
    global palavra
    global sequencia_delimitada
    global sequencia_alfabetica
    global primeira_palavra
    global DEF
    global fim_de_texto
    global numero_do_caractere
    global linha
    global linha_a_imprimir

    if status == 'inicio':
        status = 'iniciar'
        referencias = []
        ocorrencias = {}
        numero_da_linha = 0
        caractere = ''
        primeiro_caractere = False
        alfabetico = False
        palavra = ''
        sequencia_delimitada = ''
        sequencia_alfabetica = ''
        primeira_palavra = False
        DEF = False
        fim_de_texto = False
        numero_do_caractere = 0
        linha_a_imprimir = ''
        with open('fonteQ1.txt', 'r') as text_file:
            texto = text_file.read().upper().splitlines(True)
            texto.insert(0, '')
            texto[-1] = texto[-1] + '\n'
        linha = texto[numero_da_linha]

    elif status == 'finalizar':
        status = 'fim'

def p1():
    global status
    global numero_da_linha
    global caractere
    global primeiro_caractere
    global alfabetico
    global numero_do_caractere
    global linha
    global linha_a_imprimir

    if status == 'iniciar':
        if numero_do_caractere == len(linha): # linha totalmente processada
            numero_da_linha += 1
            linha = texto[numero_da_linha]
            linha_a_imprimir = str(numero_da_linha) + ' ' + linha
            numero_do_caractere = 0
            status = 'linha numerada'
        else:
            if numero_do_caractere == 0:
                primeiro_caractere = True
            else:
                primeiro_caractere = False

            if len(linha) != 0:
                caractere = linha[numero_do_caractere]
                numero_do_caractere += 1
                alfabetico = caractere.isalpha() or caractere.isdigit()
                status = 'caractere'

def p2():
    global palavra
    global status
    global sequencia_delimitada
    global primeira_palavra
    global DEF

    if 'caractere':
        if primeiro_caractere:
            primeira_palavra = True
            status = 'iniciar'
        
        if alfabetico:
            palavra += caractere
            status = 'iniciar'
        else:
            if palavra != '':
                sequencia_delimitada = palavra
                palavra = ''
                DEF = primeira_palavra
            else:
                sequencia_delimitada = caractere

            DEF = primeira_palavra
            primeira_palavra = False
            
            status = 'sequencia delimitada'

def p3():
    global sequencia_alfabetica
    global status
    global fim_de_texto

    if status == 'sequencia delimitada':

        if sequencia_delimitada.isalpha() or sequencia_delimitada.isdigit():
            sequencia_alfabetica = sequencia_delimitada
            status = 'sequencia alfabetica'
        else:
            status = 'iniciar'

        if (numero_da_linha == len(texto)-1 and numero_do_caractere == len(linha)):
            fim_de_texto = True
            status = 'tabela de referencias cruzadas'

def p4():
    global status
    global referencias
    global ocorrencias
    global DEF

    if status == 'sequencia alfabetica':
        sequencia_encontrada = False

        for referencia in referencias:
            if referencia == sequencia_alfabetica:
                if DEF:
                    ocorrencias[referencia].append(str(numero_da_linha)+'*')
                    DEF = False
                sequencia_encontrada = True
        
        if not sequencia_encontrada:
            if DEF:
                referencias.append(sequencia_alfabetica)
                ocorrencias[sequencia_alfabetica] = [str(numero_da_linha)+'*']
                DEF = False
        
        if fim_de_texto:
            status = 'tabela de referencias cruzadas'
        else:
            status = 'iniciar'

def p5():
    global status
    global referencias
    global linha_a_imprimir

    if status == 'tabela de referencias cruzadas':
        referencias.sort()

        linha_a_imprimir = '\n'
        for referencia in referencias:
            linha_a_imprimir += referencia + ' - '
            for ocorrencia in ocorrencias[referencia]:
                linha_a_imprimir += ocorrencia + ' '
            linha_a_imprimir += '\n'
        
        status = 'linha a imprimir'

def p6():
    global status

    if status == 'linha numerada':
        print(linha_a_imprimir, end='')
        status = 'iniciar'
    elif status == 'linha a imprimir':
        print(linha_a_imprimir, end='')
        status = 'finalizar'


main()