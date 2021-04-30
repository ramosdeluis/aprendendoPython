galera = []
pe = []
maiorP = []
menorP = []
while True:
    n = str(input('Digite o nome: '))
    p = float(input('Digite o peso: '))
    pe.append(n)
    pe.append(p)
    galera.append(pe[:])
    pe.clear()
    if not maiorP:
        maiorP.append(p)
    elif p > maiorP[0]:
        maiorP.pop()
        maiorP.append(p)
    if not menorP:
        menorP.append(p)
    elif p < menorP[0]:
        menorP.pop()
        menorP.append(p)
    while True:
        cont = str(input('Queres continuar adicionando pessoas? [S/N] ')).strip().upper()[0]
        if cont in 'SN':
            break
    if cont in 'N':
        break
print('-='*30)
print(f'Foram cadastradas \033[34m{len(galera)}\033[m pessoas.')
print(f'O maior peso foi {maiorP[0]:.2f} Kg. Peso de', end='')
for p in galera:
    if p[1] == maiorP[0]:
        print(f' {p[0]}', end='')
print(f'\nO menor peso foi {menorP[0]:.2f} Kg. Peso de', end='')
for p in galera:
    if p[1] == menorP[0]:
        print(f' {p[0]}', end='')
