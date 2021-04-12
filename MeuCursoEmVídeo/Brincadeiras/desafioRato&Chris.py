from random import randint


def lista():
    global li
    lil = list(set(li))
    print(f'Lista:', end=' ')
    for d in li:
        print(f'{d}', end=' ')
    print()
    for c in lil:
        print(f'{c} apareceu {li.count(c)} vezes.')


def geraLista():
    casas = randint(1, 100)
    li = []
    for c in range(0, casas):
        li.append(randint(0, 100))
    li.sort()
    return li


li = geraLista()
lista()
