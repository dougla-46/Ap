"""nu = int(input('Digite um Numero: '))
n = str(nu)

print(f'''
Unidade: {n[3]}
Dezena: {n[2]}
Centena: {n[1]}
Milhar: {n[0]}''')"""

nu = int(input('Digite um numero: '))
u = nu // 1 % 10
d = nu // 10 % 10
c = nu // 100 % 10
m = nu // 1000 % 10
print(f'''
Unidade: {u}
Dezena: {d}
Centena: {c}
Milhar: {m}''')