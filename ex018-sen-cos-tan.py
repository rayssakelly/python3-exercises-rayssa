print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.')
from math import sin, cos, tan, radians
a = float(input('Digite o valor do ângulo:'))
sen = sin(radians(a))
coss = cos(radians(a))
tang = tan(radians(a))
print('O angulo {}º, tem:\nSeno= {:.2f}\nCosseno= {:.2f}\nTangente= {:.2f}'.format(a, sen, coss, tang))
