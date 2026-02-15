from math import sqrt
from random import randint


x = randint(-10, 10)
y = randint(-10, 10)

x1 = int(input('Adivinhe o numero de x: '))
y1 = int(input('Adivinhe o numero de y: '))

d = sqrt((x - x1) ** 2 + (y - y1) ** 2 )

print(f'''
O ponto secreto de x é {x}
O ponto secreto de y é {y}
Seu chute de ambos são X: {x1} e Y: {y1}
A distancia entre oque você escolheu {d:.2f}''')