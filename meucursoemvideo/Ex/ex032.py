from datetime import date
ano = int(input('Digite um ano ou coloque "0" para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
#if ano % 4 == 0:
#    if ano % 100 != 0:
#        print('{} é um ano bissexto!'.format(ano))
#    elif ano % 400 == 0:
#        print('{} é bissexto!'.format(ano))
#    else:
#        print('{} não é bissexto.'.format(ano))
#else:
#    print('{} não é bissexto...'.format(ano))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} não é Bissexto...'.format(ano))