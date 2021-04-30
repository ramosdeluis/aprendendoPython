''' Meu jeito:
valor = int(input('Qual o valor a ser sacado? '))
valorI = valor
n50 = 0
n20 = 0
n10 = 0
n1 = 0
while True:
    while True:
        if valor < 50:
            break
        n50 += 1
        valor = valor - 50
    if valor == 0:
        break
    while True:
        if valor < 20:
            break
        n20 += 1
        valor -= 20
    if valor == 0:
        break
    while True:
        if valor < 10:
            break
        n10 += 1
        valor -= 10

    if valor == 0:
        break
    while True:
        if valor < 1:
            break
        n1 += 1
        valor -= 1

    if valor == 0:
        break
print(f'R$ {valorI:.2f}.')
if n50 > 0:
    print(f'Um total de {n50} cédulas de R$ 50,00.')
if n20 > 0:
    print(f'Um total de {n20} cédulas de R$ 20,00.')
if n10 > 0:
    print(f'Um total de {n10} cédulas de R$ 10,00.')
if n1 > 0:
    print(f'Um total de {n1} cédulas de R$ 1,00.')
Jeito da aula:
'''


print('='*30)
print('{:^30}'.format('VAMOS CALCULAR!'))
print('='*30)

valor = int(input('Digite um valor: R$ '))
total = valor
cedula = 50
totalCedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        totalCedulas += 1
        if total < cedula:
            print(f'Há um total de {totalCedulas} cédulas de R$ {cedula:.2f}')

    else:
        if total >= 20:
            cedula = 20
            totalCedulas = 0
        elif total >= 10:
            cedula = 10
            totalCedulas = 0
        elif total >=1:
            cedula = 1
            totalCedulas = 0
        elif total == 0:
            break
print('~'*30)
print('{:^30}'.format('Fim do Programa.'))
print('~'*30)








