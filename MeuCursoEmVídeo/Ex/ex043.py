p = float(input('Qual o teu peso em Kg? '))
a = float(input('Qual a tua altura em metros? '))

imc = round(p / (a**2),2)

if imc < 18.5:
    print('Abaixo do peso. IMC = {}'.format(imc))
elif imc < 25:
    print('Peso ideal. IMC = {}'.format(imc))
elif imc < 30:
    print('Sobrepeso. IMC = {}'.format(imc))
elif imc <40:
    print('Obesidade. IMC = {}'.format(imc))
else:
    print('Obesidade mórbida. IMC = {}'.format(imc))
