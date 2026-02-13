from random import shuffle, choice
print('='*3,'Digite 4 nomes Aleatorios.','='*3)
n1 = str(input('Nome: '))
n2 = str(input('Nome: '))
n3 = str(input('Nome: '))
n4 = str(input('Nome: '))
lis = [n1, n2, n3, n4]
shuffle(lis)

print('O Escolhido foi','='*2,f'{choice(lis)}','='*2)
print(f'Participantes: {lis}')

