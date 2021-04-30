s = float(input('Qual o teu salário? '))

if s > 1250:
    print('Teu novo salário será de R$ {:.2f}'.format(1.1*s))
else:
    print('Teu novo salário será de R$ {:.2f}'.format(1.15*s))
