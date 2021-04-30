pes = []
al = []
no = [0, 0, 0]
while True:
    nome = str(input('Digite o nome o aluno(a): '))
    n1 = float(input('Digite a nota 01: '))
    n2 = float(input('Digite a nota 02: '))
    no[0] = n1
    no[1] = n2
    no[2] = (n1 + n2) / 2
    al.append(nome)
    al.append(no[:])
    pes.append(al[:])
    no.clear()
    no = [0, 0, 0]
    al.clear()
    while True:
        cont = str(input('Queres continuar? [S/N] ')).strip().upper()
        if cont in 'SN':
            break
    if cont in 'N':
        break
print('-'*30)
for c in range(0, len(pes)):
    print(f'0 {c+1}º aluno é "{pes[c][0]}" e a sua média foi de {pes[c][1][2]:.2f}.')
print('-'*30)
while True:
    mos = int(input('Qual aluno desejas ver as notas? (Digite "999" para parar) '))
    if mos == 999:
        break
    elif 0 <= mos <= len(pes):
        print(f'As notas de "{pes[mos-1][0]}" foram: {pes[mos-1][1][0], pes[mos-1][1][1]}"')
    else:
        print('Não temos esse aluno registrado, tente novamente...')