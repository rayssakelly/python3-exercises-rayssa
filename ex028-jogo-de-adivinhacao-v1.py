from random import randint

print('Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.')

print('ADIVINHE MEU PENSAMENTO...')
n = (int(input('Estou pensando em um número entre 0 e 5. Qual é?:')))
m = randint(0, 5)

if n == m:
    print('Você acertou! Penesei no número {} também.'.format(m))
else:
    print('Não foi dessa vez, pensei no número {}.'.format(m))
