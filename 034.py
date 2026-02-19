sal = float(input('Digite seu Salario:R$ '))
if sal > 1250.00: # > maior / = igual

    sal1 = sal * 10 /100 #conta para % o 10 pode ser trcd para qualquer numero ou por um input
    res1 = sal + sal1 #salario + o resultado da conte de cima

    print(f'Seu salario que era R${sal} com um aumento de {sal1:.2f}(10%) vai passar a ser R${res1:.2f} ')

if sal <= 1250: # < menor

    sal2 = sal * 15 / 100
    res2 = sal + sal2

    print(f'Seu salario que era R${sal} com um aumento de {sal2:.2f}(15%) vai passar a ser R${res2:.2f} ')


"""sal3 = float(input('Digite seu Salario:R$ '))
if sal3 <= 1250:
    aum1 = sal3 + (sal3 * 15 / 100)
    print(f'Seu novo salario sera R${aum1:.2f}')
else:
    aum1 = sal3 + (sal3 * 10 / 100)
    print(f'Seu novo salario sera R${aum1:.2f}')"""