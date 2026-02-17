dig = str(input('Digite uma palavra: ')).strip().upper()

print(f'Quantas vezes a letra A aparece: {dig.count('A')}')
print(f'A letra A aparece pela Primeira vez {dig.find('A')+1}')
print(f'A letra A aparece pela ultima vez {dig.rfind('A')+1}')