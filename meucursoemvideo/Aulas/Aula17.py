num = list(range(1, 11))
print(num)
num.append(11)
print(num)
num.sort(reverse=True)
print(num)
print(f'Esta lista tem {len(num)} elementos.')
num.sort()
num.insert(3, 11)
print(num)
num.pop(2)
print(num)
num.remove(11)
print(num)
for c, valor in enumerate(num):
    print(f'Na posição {c} há {valor}')
print('Fim.')
'''valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c in range(0, len(valores)):
    print(f'{valores[c]} -> ', end='')
print('Fim')
'''
'''
a = [1, 2, 3, 4]
b = a
c = a[:]
b[2] = 12
c[3] = 57
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
'''