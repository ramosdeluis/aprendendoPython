def aumentar(n=0, v=1):
    v = (1 + 0.01 * v) * n
    tex_i = f'{v:_.2f}'
    tex_i = tex_i.replace('.', ',').replace('_', '.')
    return f'R$ {tex_i}'


def diminuir(n=0, v=0):
    v = (1 - 0.01 * v) * n
    tex_i = f'{v:_.2f}'
    tex_i = tex_i.replace('.', ',').replace('_', '.')
    return f'R$ {tex_i}'


def dobro(n=0):
    return 2 * n


def metade(n=0):
    return 0.5 * n


def moeda(n=0):
    tex_for = f'{n:_.2f}'
    tex_for = tex_for.replace('.', ',').replace('_', '.')
    return f'R$ {tex_for}'
