print('Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.')

a = float(input('Dgite o valor da 1° reta:'))
b = float(input('Dgite o valor da 2° reta:'))
c = float(input('Dgite o valor da 3° reta:'))
if a < b + c and b < a + c and c < a + b:
    print('Essas três retas podem formar um triângulo.')
else:
    print('Essas três retas NÃO podem formar um triângulo.')
