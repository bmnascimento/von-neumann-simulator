#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import vm

# Login
print('Máquina Virtual de Von Neumann v0.1')
user = input('Login: ')

while not user.isalpha():
    print('O login deve conter apenas letras')
    user = input('Login: ')

print('Bem-vindo,', user)

if not os.path.exists(user):
    os.makedirs(user)

while True:
    command = input('$ ').lower().split()

    if command[0] in ['exit', 'quit', 'q']:
        print('Adeus!')
        break

    elif command[0] == 'help':
        print('help: mostra lista de comandos disponíveis')
        print('exit, quit, q: sai do programa')
        print('dir: lista todos os programas do usuário')
        print('run <arquivo>: roda o arquivo informado, deve conter extensão')

    elif command[0] == 'dir':
        for file in os.listdir(user):
            print(file)

    elif command[0] == 'run':
        if len(command) < 2:
            print('Especifique um arquivo')

        else:
            try:
                with open(os.path.join(user, command[1]),'r') as file:
                    code = ''.join(file.read().split())
                    if '-d' in command:
                        vm.run(code, True)
                    else:
                        vm.run(code, False)

            except FileNotFoundError:
                print('Arquivo não encontrado, não se esqueça da extensão')

    else:
        print('Use comando "help" para ver lista de comandos disponíveis ou "exit" para sair do programa')

