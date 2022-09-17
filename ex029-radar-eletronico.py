print('Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.')

km = float(input('Digite a velocidade do carro:'))
if km >80:
    multa = (km - 80) * 7
    print('Você ultrapassou o limite de velocidade. Sua multa foi de {}R$'.format((multa)))


print('Tenha um bom dia! Dirija com segurança!')