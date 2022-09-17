print('Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.')

kmViagem = float(input('Digite a distância da viagem em Km:'))
if kmViagem <=200:
    ticket = kmViagem * 0.50
else:
    ticket = kmViagem * 0.45
print('O custo da sua passagem é: {:.2f}R$'.format(ticket))


