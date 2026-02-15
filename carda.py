n = str(input('Nome: '))
nu = input('Numero de Telefone: ')
end = str(input('Endereço: '))
con = str(input('Complemento: '))
ba = str(input('Bairro: '))
#n = nome. nu = numero de telefone. end = endereço. con = complemento. ba = bairro
#print vazio para espaço entre as linhas

print()
input('Aperte Enter para Confirmar')

print()
print('#'*2,'Itens do Cardapio','#'*2)
print('''
>Morangotela
>Crocante
>Trufado de Morango
>Maratella
>Ninhotella''')
print()
#ped = pedido
ped = str(input('==Qual seria o seu pedido? '))
print()
#tam = tamanho. tal = talher
print('Tamanhos: 360/480/720')
tam = int(input('Escolha o Tamanho:'))
print('Você deseja colher e guardanapo?')
tal = str(input('Sim/Não: '))
print()
print('''Metodo de Pagamento
Credito/Debito/Pix/Dinheiro''')
#pag = pagamento
pag = str(input('==Qual a forma de pagamento? '))
print()
print('='*3,'Informações do Cliente','='*3)

print(f'''
Nome: {n}
Numero de Telefone: {nu}
Endereço: {end}
Complemento: {con}
Bairro: {ba}''')
print()

print('-'*3,'Itens do Pedido','-'*3)
print(f'''{ped} {tam}ml
{tal}, desejo colher e guardanapo!''')
print()
print('='*3,'Forma de Pagamento','='*3)
print('>',f'{pag}')