print('Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome')
sobrenome = str(input('Digite seu nome completo:')).strip().upper()
print('Seu nome tem Silva?{}'.format('SILVA' in sobrenome))