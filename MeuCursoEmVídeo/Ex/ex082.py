num = []
pars = []
imps = []
'''
while True:
    n = int(input('Digite um valor: '))
    if n % 2 ==0:
        num.append(n)
        pars.append(n)
    else:
        num.append(n)
        imps.append(n)
    while True:
        cont = str(input('Queres continuar? [S/N] ')).strip().upper()
        if cont in 'SN':
            break
    if cont in 'N':
        break
if len(num) == 1:
    print(f'Só foi digitado o valor: {num[0]}')
else:
    print(f'Os números digitados foram: {num}')
if len(pars) == 0:
    print('Não foram digitados números pares.')
else:
    print(f'O números pares digitados foram: {pars}')
if len(imps) == 0:
    print('Não foram digitados números ímpares.')
else:
    print(f'Os números ímpares digitados foram: {imps}')
'''

while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    while True:
        cont = str(input('Queres continuar? [S/N] ')).strip().upper()
        if cont in 'SN':
            break
    if cont in 'N':
        break

for c in num:
    if c % 2 == 1:
        imps.append(c)
    else:
        pars.append(c)

if len(num) == 1:
    print(f'Só foi digitado o valor: {num[0]}')
else:
    print(f'Os números digitados foram: {num}')
if len(pars) == 0:
    print('Não foram digitados números pares.')
else:
    print(f'O números pares digitados foram: {pars}')
if len(imps) == 0:
    print('Não foram digitados números ímpares.')
else:
    print(f'Os números ímpares digitados foram: {imps}')