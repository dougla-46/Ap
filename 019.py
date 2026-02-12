from random import choice

a1 = str(input('Nome do 1º Aluno: '))
a2 = str(input('Nome do 2º Aluno: '))
a3 = str(input('Nome do 3º Aluno: '))
a4 = str(input('Nome do 3º Aluno: '))
lis = [a1, a2, a3, a4]

es = choice(lis)

print('='*3,f'O Escolhido foi {es}','='*3)

