'''
from datetime import date


def voto(ano):
    idade = date.today().year - ano
    if idade >= 65:
        return 'voto opcional'
    elif idade >= 18:
        return 'voto obrigatório'
    elif idade >= 16:
        return 'voto opcional'
    else:
        return 'voto negado'


# Programa Principal
nasc = int(input('Qual o ano de nascimento: '))
print(f'Com {date.today().year-nasc} anos: {voto(nasc)}.')
'''
def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: voto inválido.'
    if 18 > idade >= 16 or idade > 65:
        return f'Com {idade} anos: voto opcional.'
    else:
        return f'Com {idade} anos: voto obrigatório.'


nas = int(input('Em que ano tu nasceste? '))
print(voto(nas))