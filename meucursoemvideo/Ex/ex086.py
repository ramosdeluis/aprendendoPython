'''
lin = [[], [], [], [], [], [], [], [], []]
for c in range(0, 3):
    lin[c].append(int(input(f'Digite o valor para [0, {c}]: ')))
    lin[c+3].append(int(input(f'Digite o valor para [1, {c}]: ')))
    lin[c+6].append(int(input(f'Digite o valor para [2, {c}]: ')))
print('-='*20)
for c in range(0, 9):
    print(f'{lin[c]}', end='')
    if (c + 1) % 3 == 0:
        print('\n')
'''

lin = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for e in range(0, 3):
    for d in range(0, 3):
        lin[e][d] = int(input(f'Digite o valor [{e}, {d}]: '))
print('-'*30)
for e in range(0, 3):
    for d in range(0, 3):
        print(f'[{lin[e][d]:^4}]', end='')
    print()