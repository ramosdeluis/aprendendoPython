from random import randint
from time import sleep
l = int(input('Quantas listas queres ver? '))
for d in range(0, l):
    num = []
    nnl = randint(1, 10)
    for v in range(0, nnl):
        num.append(randint(0, 10))


    def maior(num):
        ma = 0
        cont = 1
        for v in num:
            if cont == 1:
                ma = v
                cont += 1
            else:
                if v > ma:
                    ma = v
        print('-='*30)
        print(f'{d+1}ª lista.', end=' ')
        print(f'Analisando os valores...')
        for c in num:
            print(f'{c}', end=' ')
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior número informado foi o {ma}.')


    maior(num)
    sleep(0.5)