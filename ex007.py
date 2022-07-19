print('Leia duas notas e mostre a media entre elas')
print('Olá aluno!')
print('Usando . para representar numéros depois da vírgula:')
n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
s = (n1 + n2)
m = s / 2
print('O total das suas notas foi {:.2f}.\nA media aritmética foi {:.2f}.\n'.format(s, m))
