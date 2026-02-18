pre = int(input('Quantos Kms vai ter na sua viagem?'))#Uma kilometragem aleatoria
if pre <= 200:#< quer dizer menor que
    mnd = pre * 0.50# pre * o valor da kilometragem
    print(f'A sua viagem de {pre}Kms vai ficar R${mnd:.2f}')
if pre >= 201:#> quer dizer maior que
    mnd1 = pre * 0.45
    print(f'A sua viagem de {pre}Kms vai ficar R${mnd1:.2f}')

