print('Leia o preço de um produto e depois mostre com 5% de desconto')
op = float(input('Digite o valor original do produto:R$'))
dp = op - (op * 0.05)
print('O valor original do seu produto é R${:.2f} \nCom desconto de 5% sai por R${:.2f}'.format(op, dp))