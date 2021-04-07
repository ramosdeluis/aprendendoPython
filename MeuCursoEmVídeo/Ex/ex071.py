valor = int(input('Qual o valor a ser sacado? '))
valorI = valor
n50 = 0
n20 = 0
n10 = 0
n1 = 0
while valor != 0:
    while True:
        n50 += 1
        valor -= 50
        if valor < 50:
            break
    if valor == 0:
        break
    while True:
        n20 += 1
        valor -= 20
        if valor < 20:
            break
    if valor == 0:
        break
    while True:
        n10 += 1
        valor -= 10
        if valor < 10:
            break
    if valor == 0:
        break
    while True:
        n1 += 1
        valor -= 1
        if valor < 1:
            break
    if valor == 0:
        break
print(f'R$ {valorI:.2f}.')
print(f'Um total de {n50} cédulas de R$ 50,00.')
print(f'Um total de {n20} cédulas de R$ 20,00.')
print(f'Um total de {n20} cédulas de R$ 10,00.')
print(f'Um total de {n1} cédulas de R$ 1,00.')