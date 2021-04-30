def fatorial(num=0, show=False):
    """
     -> Calcula o fatorial de um número
    :param num: número a ser calculado o fatorial
    :param show: se queres a conta ou só o resultado
    :return: conta inteira ou só o resultado
    """
    tot = 1
    for v in range(num, 0, -1):
        tot *= v
        if show is True:
            print(f'{v}', end=' ')
        if v != 1 and show is True:
            print('x ', end=' ')
    if show is True:
        print('=', end=' ')
    print(f'{tot}')
    return ''



# Programa Principal
print(fatorial(9, True))