def leiaInt(msg):
    while True:
        try:
            v = int(input(msg))
        except:
            print(f'\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return v


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc