from random import randint
dupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('~'*40)
print('Os números sorteados foram: ', end='')
for c in range(0, 5):
    print(f'{dupla[c]}', end=' ')
print('')
print('~'*40)
maior = menor = cont = 0
for c in range(0, 5):
    if cont == 0:
        maior = menor = dupla[c]
        cont += 1
    elif dupla[c] > maior:
        maior = dupla[c]
        cont += 1
    elif dupla[c] < menor:
        menor = dupla[c]
        cont += 1
print(f'O maior número foi \033[34m{maior}\033[m.')
print(f'O menor número foi \033[33m{menor}\033[m.')