n = str(input('Digite seu nome completo:')).strip()
m = n.split()
print(f'''
Seu nome todo em Maisculo: {n.upper()}
Seu nome em Minusculo: {n.lower()}
Quantas letras tem em seu nome (desconsiderando os espaços): {len(n) - n.count(' ')}
Quantas letras tem o primeiro nome: {len(m[0])}''')


