print('Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o '
      'primeiro e o último nome separadamente')
nome = str(input('Digite seu nome completo:')).strip()
n = nome.split()
print('Seu primeiro nome é:{}'.format(n[0].capitalize()))
print('Seu ultimo nome é: {}'.format(n[len(n)-1].capitalize()))