li = []
pessoa = {}
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    pessoa['idade'] = int(input('Idade: '))
    li.append(pessoa.copy())
    pessoa.clear()
    while True:
        cont = str(input('Queres continuar? [S/N] ')).strip().upper()
        if cont in 'SN':
            break
    if cont in 'N':
        break
mediaI = 0
for v in li:
    mediaI += v['idade']
mediaI = mediaI / len(li)
print('-='*35)
print(f'Foram cadastradas {len(li)} pessoas.')
print(f'A média de idade é de {mediaI:.2f} anos.')
print(f'As mulheres são: ', end='')
for v in li:
    if v['sexo'] in 'F':
        print(f' {v["nome"]}', end='')
print()
for p in li:
    if p['idade'] > mediaI:
        print(f'Nome = {p["nome"]}; Sexo = {p["sexo"]}; Idade = {p["idade"]};')
print('-='*35)
print(f'{"Fim do Programa":^70}')