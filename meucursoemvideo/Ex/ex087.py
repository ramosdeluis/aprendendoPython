mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for e in range(0, 3):
    for d in range(0, 3):
        mat[e][d] = int(input(f'Digite o falor de [{e}, {d}]: '))
print('-'*30)
for e in range(0, 3):
    for d in range(0, 3):
        print(f'[{mat[e][d]:^5}]', end='')
    print()
print('-'*30)
somaPares = soma3Col = maior2Lin = 0
for e in range(0, 3):
    for d in range(0, 3):
        if mat[e][d] % 2 == 0:
            somaPares += mat[e][d]
        if mat[e][2]:
            soma3Col += mat[e][2]
        if e == 1 and d == 0:
            maior2Lin = mat[e][d]
        elif e == 1 and mat[e][d] > maior2Lin:
            maior2Lin = mat[e][d]
print(f'A soma dos pares é: {somaPares}')
print(f'A soma dos valores da terceira coluna é: {soma3Col/3:.0f}')
print(f'O maior valor da segunda linha é: {maior2Lin}')