dupla = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')),
         int(input('Digite outro valor: ')), int(input('Digite o último valor: ')))
'''noves = 0
pares = ''
for c in range(0, 4):
    if dupla[c] == 9:
        noves += 1
    if dupla[c] % 2 == 0:
        pares += f' {dupla[c]}'
print('~'*40)
print(f'Vocês digitou os valores: ', end='')
for c in dupla:
    print(f'{c} ', end= '')
print('\n'+'~'*40)
print(f'O "9" apareceu um total de {noves} vezes.')
print('~'*40)
if 3 in dupla:
    print(f'O primeiro 3 apareceu na posição {dupla.index(3)+1}.')
else:
    print('Não foi digitado nenhum valor 3.')
print('~'*40)
if pares != '':
    print(f'Os números pares digitados foram{pares}.')
else:
    print('Não foi digitado nenhum número par.')
print('~'*40)
'''
print(f'Você digitou os valores: {dupla}')
print(f'O valor "9" apareceu {dupla.count(9)} vezes.')
if 3 in dupla:
    print(f'O primeiro três aparece na {dupla.index(3)+1}ª posição.')
else:
    print('Não há nenhum três dentre os números digitados.')
pares = 0
for c in dupla:
    if c % 2 == 0:
        pares += 1
if pares != 0:
    print('Os números pares são: ', end='')
    for c in dupla:
        if c % 2 == 0:
            print(c, end=' ')
else:
    print('Não há nenhum número par.')
