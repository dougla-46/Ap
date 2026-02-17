"""c = str(input('Em que cidade você nasceu? '))
print('Santo' in c)"""

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

