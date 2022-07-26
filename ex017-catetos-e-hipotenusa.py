print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.')
from math import hypot
co = float(input('Digite o valor do Cateto Oposto:'))
ca = float(input('Digite o valor do Cateto Adjacente:'))
hip = hypot(co,ca)
print('O triângulo retângulo Cateto adjacente= {} e cateto oposto= {}\nTem Hipotenusa= {:.2f}.'.format(ca, co, hip))

print('\n')
 #Sem o uso dos modúlos
catop = float(input('Digite o valor do cateto oposto:'))
catad = float(input('igite o valor do cateto adjacente:'))
hipot = ((catop * catop + catad * catad) ** 0.5 )
print('O triângulo retângulo Cateto adjacente= {} e cateto oposto= {}\nTem Hipotenusa= {:.2f}.'.format(catop, catad, hipot))