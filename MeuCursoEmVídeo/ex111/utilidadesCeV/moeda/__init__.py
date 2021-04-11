def aumentar(n=0, v=1, para=True):
    v = (1 + 0.01 * v) * n
    return v if not para else moeda(v)


def diminuir(n=0, v=0, para=True):
    v = (1 - 0.01 * v) * n
    return v if not para else moeda(v)


def dobro(n=0, para=True):
        return 2 * n if not para else moeda(2*n)


def metade(n=0, para=True):
        return 0.5 * n if not para else moeda(0.5*n)


def moeda(n=0):
        tex_for = f'{n:_.2f}'
        tex_for = tex_for.replace('.', ',').replace('_', '.')
        return f'R$ {tex_for}'


def resumo(n, a, r):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n)}')
    print(f'Metade do preço: \t{metade(n)}')
    print(f'{a}% de aumento: \t\t{aumentar(n, a)}')
    print(f'{r}% de redução: \t{diminuir(n, r)}')
    print('-'*30)