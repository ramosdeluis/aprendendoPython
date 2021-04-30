num = []
for c in range(0, 5):
    num.append(int(input('Digite um valor: ')))
print(f'O maior número digitado foi {max(num)}, que está na posição', end='')
for pos, valor in enumerate(num):
    if valor == max(num):
        print(f' {pos}...', end='')
print(f'\nO menor número digitado foi {min(num)}, que está na posição', end='')
for pos, valor in enumerate(num):
    if valor == min(num):
        print(f' {pos}...', end='')