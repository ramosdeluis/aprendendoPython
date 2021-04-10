# Funções - 1

# Funções
def soma(a, b):
    print(f'{a} + {b} = {a+b}')

'''
# Programa principal
soma(b=4, a=5)
soma(8, 9)
soma(2, 1)
'''
'''
def contador(* núm):
    for v in núm[:-1]:
        

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''
'''
valo = (5, 7, 4, 2, 9, 20)


def dobra(lst):
    cont = 0
    while cont < len(lst):
        lst[cont] *= 2
        cont += 1


def soma(*ttt):
    s = 0
    for d in ttt:
        s += d
    print(f'A soma de {ttt} é {s}.')


valores = [5, 7, 4, 2, 9, 20]

soma(*valo)
print(valores)
dobra(valores)
soma(*valo)
print(valores)
'''
núm = (0, 2, 5, 7, 9)
dobro = []


def dobrar(*n):
    for v in range(0, len(núm)):
        dobro.append(núm[v]*2)


dobrar(núm)
print(dobro)
