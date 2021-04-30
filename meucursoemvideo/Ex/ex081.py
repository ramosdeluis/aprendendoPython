lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    while True:
        cont = str(input('Queres continuar digitando valores? [S/N] ')).strip().upper()[0]
        if cont in 'SN':
            break
    if cont in 'N':
        break
print(f'Foram digitados {len(lista)} números.')
if 5 in lista:
    print(f'O valor "5" foi digitado e apareceu a primeira vez na posição {lista.index(5)+1}.')
else:
    print(f'O "5" não foi digitado...')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente foca: {lista}')