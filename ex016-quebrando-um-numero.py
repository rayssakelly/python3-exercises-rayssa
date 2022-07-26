print ('Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.')
from math import trunc
n = float(input('Digite um número Real:'))
r = trunc(n)
print('O valor digitado é {}, sua parte inteira é {}.'.format(n, r))

#Sem utilizar o modo apenas use a função int.

nf = float(input('Digite um número Real:'))
ni = int(nf)
print('O valor digitado foi {} e sua parte inteira é {}.'.format(nf, ni))