print('Ler um numero e mostar quantos dolares pode-se comprar, considerando US$1,00 = R$ 3,27')
print('Use ponto "." para indicar números depois da vírgula.')
r = float(input('Quantos Reais você tem?R$:'))
d = r / 3.27
print('Com R${:.2f} você consegue comprar, U$D{:.2f} dólares.'.format(r, d))