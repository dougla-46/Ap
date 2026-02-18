vel = int(input('Qual era a velocidade do carro? '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você foi MULTADO!!!')
    print(f'Sua multa por dirigir a {vel} vai ser de R$ {multa}')