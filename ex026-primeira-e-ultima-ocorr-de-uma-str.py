print('Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece '
      'a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.')
letA = str(input('Digite uma frase:')).lower().strip()
print('ANALISANDO...')
print('Na sua frase, a letra A aparece {} vezes.'.format(letA.count('a')))
print('A letra A aparece em sua frase primeiramente na {}º posição'.format(letA.find('a')+1)) #o +1, é para que a primeira posiçaõ seja 1, não zero como sabemos.#
print('A letra A aparece em sua frase pela última vez na {}º posição'.format(letA.rfind('a')+1))

