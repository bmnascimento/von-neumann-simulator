import os

import interpretador
import vm
import montador

job = ''
pwd = os.path.join(os.getcwd(), 'teste')
infile = 'teste_in'
outfile = 'teste_out'
diskfile = 'teste_disk'

while (True):
    event = input('> ').split(' ')
    event[0] = event[0].lower()
    #print(event)

    if event[0] == '$job':
        try:
            job = event[1]
            pwd = os.getcwd()
            infile = ''
            outfile = ''
            diskfile = ''
            print('Iniciado o job', job)
        except IndexError:
            print('Especifique um job')

    elif event[0] == '$disk':
        try:
            pwd = os.path.join(pwd, event[1])
        except IndexError:
            print('Especifique um diretório')

    elif event[0] == '$directory':
        for item in os.listdir(pwd):
            print(item)

    elif event[0] == '$create':
        try:
            f = open(os.path.join(pwd, event[1]), 'x')
            f.close()
        except FileExistsError:
            print('Arquivo já existe')
        except IndexError:
            print('Especifique o nome do arquivo')

    elif event[0] == '$delete':
        try:
            os.remove(os.path.join(pwd, event[1]))
        except IndexError:
            print('Especifique o nome do arquivo')
        except FileNotFoundError:
            print('Arquivo não encontrado')
        except IsADirectoryError:
            print('Nome especificado é um diretório e não um arquivo')

    elif event[0] == '$list':
        try:
            with open(os.path.join(pwd, event[1]), 'r') as f:
                for line in f.readlines():
                    print(line, end='')
                print()
        except IndexError:
            print('Especifique o nome do arquivo')
        except FileNotFoundError:
            print('Arquivo não encontrado')

    elif event[0] == '$infile':
        try:
            infile = event[1]
            print('Infile:', infile)
        except IndexError:
            print('Especifique um arquivo')

    elif event[0] == '$outfile':
        try:
            outfile = event[1]
            print('Outfile:', outfile)
        except IndexError:
            print('Especifique um arquivo')

    elif event[0] == '$diskfile':
        try:
            diskfile = event[1]
            print('Diskfile:', diskfile)
        except IndexError:
            print('Especifique um arquivo')

    elif event[0] == '$run':
        try:
            with open(os.path.join(pwd, diskfile), 'r') as diskfile_obj:
                with open(os.path.join(pwd, infile), 'r') as infile_obj:
                    with open(os.path.join(pwd, outfile), 'w') as outfile_obj:
                        if event[1] == 'vm':
                            saida = vm.main(diskfile_obj.read(), infile_obj.read(), False)
                            outfile_obj.write(saida)
                        elif event[1] == 'montador':
                            saida = montador.montador(infile_obj.read(), infile_obj.read())
                            outfile_obj.write(saida)
                        elif event[1] == 'interpretador':
                            saida = interpretador.run(diskfile_obj.read(), infile_obj.read())
                            outfile_obj.write(saida)
        #except IndexError:
        #    print('Especifique um programa')
        except FileNotFoundError:
            print('Arquivo não encontrado')

    elif event[0] == '$endjob':
        print('Até logo!')
        break

    else:
        if len(event[0]) > 0:
            print(event[0], 'não é um programa conhecido')
            if event[0][0] != '$':
                print('Não se esqueça do $')
