print('O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')
from random import shuffle
aluno1 = str(input('Digite o nome do preimeiro aluno:'))
aluno2 = str(input('Digite o nome do segundo aluno:'))
aluno3 = str(input('Digite o nome do terceiro aluno:'))
aluno4 = str(input('Digite o nome do quarto aluno:'))
apresent =[aluno1, aluno2, aluno3, aluno4]
shuffle(apresent)
print('A ordem de apresentação do trabalho será:')
print(apresent)

