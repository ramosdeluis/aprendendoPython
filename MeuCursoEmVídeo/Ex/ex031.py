d = float(input('Qual a distância da viagem? '))

if d > 200:
    print('O preço da passagem será de R$ {:.2f}'.format(d*0.45))
else:
    print('O preço da passagem será de R$ {:.2f}'.format(d*0.5))
