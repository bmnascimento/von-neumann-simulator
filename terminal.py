#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Máquina Virtual de Von Neumann v0.1')
login = input('Login: ')
print('Bem-vindo,', login)

while True:
    command = input('$ ')

    if command.lower() == 'exit':
        print('Adeus!')
        break
