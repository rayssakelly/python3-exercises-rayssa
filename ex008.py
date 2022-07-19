print('Ler uma medida em metros e converta para centimétros e milimetros.')
m = float(input('Digite a medida que deseja converter:'))
cm = m * 100
mm = m * 1000
print('A medida de {} metros \n Equivale a: \n {:.2f} cm \n {:.2f} mm'.format( m, cm, mm))