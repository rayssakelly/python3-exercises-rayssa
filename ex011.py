print('Leia a largura da parede e calcule a tinta nescessaria para pinta-lá, sabendo que 1l de tinta pinta 2m².')
l = float(input('Qual largura da parede a ser pintada:'))
h = float(input('Qual altura da parede a ser pintada:'))
mq = l * h
t = mq / 2
print('Pra pintar sua parede de {}m², você prescisrá de {}L de tinta.'.format(mq, t))