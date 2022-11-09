#print('''Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

#– O primeiro valor é maior

#– O segundo valor é maior

#– Não existe valor maior, os dois são iguais''')

print('#' * 30)
print('COMPARADOR DE NÚMEROS')
print('#' * 30)
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
if n1 > n2:
    print('O primeiro valor {} é o maior.'.format(n1))
elif n1 < n2:
    print('O segundo valor {} é o maior.'.format(n2))
else:
    print('Não exite valor maior, os dois são iguais.')