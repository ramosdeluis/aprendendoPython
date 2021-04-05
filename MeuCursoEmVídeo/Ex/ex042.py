a = float(input('Digite uma reta:'))
b = float(input('Digite uma reta:'))
c = float(input('Digite uma reta:'))

if a <  b + c and b < c + a and c < a + b:
    print('As retas {}, {}, {} formam um triângulo.'.format(a, b, c))
    if a == b == c:
        print('O triângulo é equilátero.')
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        print('O triângulo é isóceles.')
    else:
        print('É um triângulo escaleno.')
else:
    print('A três retas ({},{},{}), não formam um trinângulo.'.format(a, b, c))