from datetime import date
numMaiores = 0
numMenores = 0
for c in range(1, 8):
    ano = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(c)))
    if date.today().year - ano >= 21:
        numMaiores += 1
    else:
        numMenores += 1

print('O número de maiores é: {}.'.format(numMaiores))
print('O número de menores é: {}.'.format(numMenores))
