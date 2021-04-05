a = float(input('Digite uma reta:'))
b = float(input('Digite uma reta:'))
c = float(input('Digite uma reta:'))

if a <  b + c and b < c + a and c < a + b:
    print('As retas {}, {}, {} formam um triângulo.'.format(a, b, c))
    if a == b == c:
        print('O triângulo é \033[34mequilátero\033[m.')
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        print('O triângulo é \033[34misóceles\033[m.')
    else:
        print('É um triângulo \033[34mescaleno\033[m.')
else:
    print('A três retas ({},{},{}), não formam um trinângulo.'.format(a, b, c))