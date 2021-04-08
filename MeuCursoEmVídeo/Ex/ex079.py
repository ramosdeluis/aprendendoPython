num = []
'''
while True:
    num.append(int(input('Digite um número: ')))
    if num[-1] in num[:-1]:
        num.pop(-1)
        print('Valor duplicado, não vou adicionar.')
    while True:
        cont = str(input('Queres continuar? [S/N] ')).strip().upper()[0]
        if cont in 'SN':
            break
        print('Opção inválida.', end='\n')
    if cont in 'N':
        break
num.sort()
print(f'{num}')
'''
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicioná-lo.')
    while True:
        c = str(input('Queres continuar? [S/N] ')).strip()
        if c in 'SsNn':
            break
    if c in 'Nn':
        break
print('-'*30)
num.sort()
print(f'Vocês digitou os valores: {num}')
print('-'*30)
print('{:^30}'.format('FIM DO PROGRAMA'))