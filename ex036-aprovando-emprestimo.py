print('Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.')
casa = float(input('Qual preço da casa:R$'))
renda = float(input('Renda mensal do comprador:R$'))
prazo = int(input('Prazo em anos para quitar o finacimento:'))
financimento = ((casa) / (prazo * 12))
prestacao = ((renda) * 0.3)

print('O fianciamento da sua casa, no preço de R${}, terá prestação mensal de R${:.2f} e sera quitado em {} anos.'.format((casa), (financimento), (prazo)))

if financimento <= prestacao:
    print('EMPRÉSTIMO APROVADO!')
else:
    print('EMPRÉSTIMO NEGADO!')

