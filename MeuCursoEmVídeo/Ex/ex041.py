from datetime import date
print('=-='*9)
print('{}'.format('Classificação de Natação!'))
print('=-='*9)

ano = int(input('''Qual o teu ano de nascimento?
'''))

idade = date.today().year - ano

if idade <= 9:
    print('Categoria: MIRIM')
elif idade > 9 and idade <= 14:
    print('Categoria: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Categoria: JÚNIOR')
elif idade > 19 and idade <= 20:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')

