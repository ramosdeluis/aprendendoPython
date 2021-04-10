from time import sleep


def contador(ini, fim, passo):
    print('-=' * 20)
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}.')
    if passo > 0:
        if ini < fim:
            for v in range(ini, fim + 1, passo):
                print(f'{v}', end=' ')
                sleep(0.1)
        elif fim < ini:
            for v in range(ini, fim - 1, -passo):
                print(f'{v}', end=' ')
                sleep(0.1)
        else:
            print('Os valores são iguais.')
    elif passo < 0:
        if ini < fim:
            for v in range(ini, fim +1, -passo):
                print(f'{v}', end=' ')
                sleep(0.1)
        elif fim < ini:
            for v in range(ini, fim - 1, passo):
                print(f'{v}', end=' ')
                sleep(0.1)
        else:
            print('Os valores são iguais.')
    else:
        if ini < fim:
            for v in range(ini, fim + 1, 1):
                print(f'{v}', end=' ')
                sleep(0.1)
        elif fim < ini:
            for v in range(ini, fim - 1, -1):
                print(f'{v}', end=' ')
                sleep(0.1)
        else:
            print('Os valores são iguais.')
    print(f'FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é a tua vez!')
início = int(input('Início: '))
final = int(input('Fim: '))
pas = int(input('Passo: '))
contador(início, final, pas)
print('-='*20)
print(f'{"Fim do Programa, volte sempre.":^20}')