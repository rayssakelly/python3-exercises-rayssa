print('Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”')
cidade = str(input('Digte o nome da sua cidade:')).strip().lower()
santo = 'santo'
print((cidade.split()[0]) == (santo))
