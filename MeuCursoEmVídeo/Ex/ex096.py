def calculo(a, b):
    area = a*b
    print(f'A área total de {l:.2f} m X {c:.2f} m é: {area:.2f} m².')


l = float(input('Digite a largura do terreno em metros: '))
c = float(input('Digite o comprimento do terreno em metros: '))
calculo(l, c)
