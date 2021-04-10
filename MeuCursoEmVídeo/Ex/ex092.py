from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = date.today().year - int(input('Ano de nascimento: '))
pessoa['CTPS'] = int(input('Carteira de trabalho (0 para caso não tenhas): '))
if pessoa['CTPS'] != 0:
    pessoa['ano de contratação'] = int(input('Qual o ano de contratação? '))
    pessoa['salário'] = float(input('Qual o salário? R$ '))
    pessoa['se aposenta'] = pessoa['idade'] + 35 - (date.today().year - pessoa['ano de contratação'])
else:
    del pessoa['CTPS']
for v, k in pessoa.items():
    print(f'{v.title()} é igual a {k}.')