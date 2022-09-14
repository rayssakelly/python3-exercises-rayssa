print('''Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome''')

nome = input(str('Qual seu nome?')).strip()
print('analisando...')
print('Esse é seu nome com letras maiúsculas:{}'.format(nome.upper()))
print('Esse é seu nome com letras minúsculas:{}'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome)-nome.count(' '))) #função len conta os carcteres, função count retira oque esta no parentese.
separa = nome.split()[0]
print('Seu primeiro nome {} tem {} letras.'.format(separa.capitalize(), len(separa)))


