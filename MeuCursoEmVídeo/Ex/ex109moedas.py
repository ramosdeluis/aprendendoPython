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
