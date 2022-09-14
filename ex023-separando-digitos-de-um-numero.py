#print('Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.')
#STRING
#num = str(input('Digite um numero entre 0 e 9999:'))
#print('Seu numéro contém:')
#print('{} Unidades'.format(num.split()[3]))
#print('{} Dezenas'.format(num.split()[2]))
#print('{} Centenas'.format(num.split()[1]))
#print('{} Milhares'.format(num.split()[0]))

print('Forma Numérica:')
numer = int(input('Digite um numero entre 0 e 9999:'))
u = numer // 1 % 10
d = numer // 10 % 10
c = numer // 100 % 10
m = numer // 1000 % 10
print('Seu numéro contém:')
print('Unidades: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhar: {}'.format(m))