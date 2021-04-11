def notas(*n, sit=False):
    d = {}
    c = 0
    m = 0
    d['Nº de notas'] = len(n)
    for v in n:
        m += v
        if c == 0:
            d['maior'] = v
            d['menor'] = v
            c += 1
        else:
            if v < d['menor']:
                d['menor'] = v
            if v > d['maior']:
                d['maior'] = v
            c += 1
    d['média'] = m / len(n)
    if sit:
        if d['média'] >= 7:
            d['situação'] = 'BOA'
        elif d['média'] >= 5:
            d['situação'] = 'RAZOÁVEL'
        else:
            d['situação'] = 'RUIM'
    return d


# Programa Principal
resp = notas(3.5, 1, 7, 6.5, 9.9, 10, 10, 10, 0, sit=True)
print(resp)
