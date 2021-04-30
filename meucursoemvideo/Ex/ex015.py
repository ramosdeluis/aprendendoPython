d = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))
t = 60 * d + 0.15 * km
print('O valor a ser pago será de R$ {:.2f}'.format(t))
