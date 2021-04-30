v = float(input('Qual a velocidade do carro, em Km/h? '))

if v > 80:
    print('Tu foste multado em R$ {:.2f}'.format((v-80)*7))
else:
    print('Que bom, dentro dos limites de velocidade :).')
