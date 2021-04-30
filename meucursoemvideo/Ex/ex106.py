"""
def manual(com=''):
    def dig(a):
        from time import sleep
        sleep(0.3)
        print('~'*(len(a)+4))
        print(f'  {a}')
        print('~'*(len(a)+4))


    while True:
        if com == '':
            com = 'Sistema De Ajuda PyHelp'
            dig(com)
            d = str(input('Função ou Biblioteca > '))
        elif d.strip().upper() == 'FIM':
            break
        else:
            if help(d):
                dig(f'Acessando o manual do comando "{d}"')
                dig(f'{help(d)}')
                com = ''
            else:
                dig(f'"{d}" não foi encontrado no sistema. Tente novamente.')
                com = ''
    print('FIM')
"""
from time import sleep
c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[7;30m',)


def ajuda(str):
    título(f'Acessando o manual do comando \'{str}\'', 4)
    print(c[5], end='')
    help(str)
    print(c[0], end='')
    sleep(0.8)


def título(msg, cor=0):
    print(c[cor], end='')
    print('~'*(len(msg)+4))
    print(f'  {msg}')
    print('~'*(len(msg)+4))
    print(c[0], end='')
    sleep(0.5)

# Programa principal
comando = ''
while True:
    título('Sistema de Ajuda PyHelp', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.strip().upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Até Logo!', 2)