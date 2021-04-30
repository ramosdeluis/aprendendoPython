from random import randint


def sorteia():
    números = []
    for c in range(0, 5):
        números.append(randint(0, 10))
    somaP = somaPar(números)
    print(f'Foram sorteados {len(números)} valores:', end=' ' )
    for d in números:
        print(f'{d}', end=' ')
    print('PRONTO!')
    print(f'Somando os valores pares de {números}, nós temos: {somaP}!')


def somaPar(num):
    somaP = 0
    for c in range(0, len(num)):
        if num[c] % 2 == 0:
            somaP += num[c]
    return somaP


sorteia()