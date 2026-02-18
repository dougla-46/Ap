import random

x = int(input('Tente adivinhar o numero: '))
ran = random.randint(0, 5)
if ran == x:
    print('Parabens! Você acertou!')
else:
    print('Você errou! O computador venceu!')

