print('Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.')

salario1 = float(input('digite seu slário atual:'))
if salario1 <= 1250.00:
    salario2 = salario1 * 0.15
else:
    salario2 = salario1 * 0.10
print('Seu aumento salárial sera {:.2f} reais, totalizando R${:.2f}'.format((salario2), (salario1 + salario2)))