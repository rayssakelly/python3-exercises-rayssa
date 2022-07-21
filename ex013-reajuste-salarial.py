print('Leia o salário de um funcionario e mostre o novo valor com 15 % de aumento.')
os = float(input('Digite o salário atual:'))
ns = os + os * 0.15
print('O novo salário do funcionario é R${:.2f}'.format(ns))