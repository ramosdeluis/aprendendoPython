cont = 'Ss'
total = 0
maisDe1 = 0
maisBarato = ''
precoMaisB = 0
while True:
    nome = str(input('Nome: '))
    preco = float(input('Preço: R$  '))
    total += preco
    if preco > 1000:
        maisDe1 += 1
    if maisBarato == '' or precoMaisB > preco:
        maisBarato = nome
        precoMaisB = preco
    while True:
        cont = str(input('Queres continuar? [S/N] '))
        if cont in 'NnSs':
            break
    if cont in 'Nn':
        break
    print('-'*30)
print('-'*30)
print('Fim do programa!')
print(f'O total gasto foi de R$ {total:.2f}')
print(f'{maisDe1} produtos custam mais de R$ 1.000,00')
print(f'O produto mais barato é o "{maisBarato}", por R$ {precoMaisB:.2f}.')
