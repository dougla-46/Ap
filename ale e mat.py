from math import sqrt, ceil, floor
from random import randint

ale = randint(1, 100)
input('Aperte enter para gerar um numero aleatorio entre 1 e 100')
print(f'Numero Gerado: {ale}')
raiz = sqrt(ale)

print(f'''A raiz quadrada de {ale} é {raiz:.2f}
{raiz:.2f} arredondado para cima é {ceil(raiz):.2f}
{raiz:.2f} arredondado para baixo é {floor(raiz):.2f}''')