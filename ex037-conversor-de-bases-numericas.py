print('Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.')
print('-' * 30)
print('CONVERSOR DE BASES NUMÉRICAS')
print('-' * 30)
n = int(input('Digite o número que deseja converter:'))
print('[1]Converter para BINÁRIO.\n[2]Converter para OCTAL.\n[3]Converter para HEXADECIMAL.')
convert = int(input('Sua opção é:'))
if convert == 1:
    print((bin(n))[2:])
elif convert == 2:
    print((oct(n))[2:])
elif convert == 3:
    print((hex(n))[2:])
else:
    print('VALOR INVÁLIDO.')





