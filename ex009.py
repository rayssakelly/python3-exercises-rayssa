print('Leia qualquer numero e mostre tabuada')
n = int(input('Digite um numero, para saber sua tabuada:'))

for i in (range(11)):
    mult = n * i
    print('{}x{}={}'.format(n,i,mult))