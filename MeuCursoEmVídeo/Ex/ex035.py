r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite o comprimento de uma reta: '))
r3 = float(input('Digite o comprimento de uma reta: '))

if r1 > r2 and r1 > r3:
    if (r2 + r3) > r1:
        print('Os catetos {:.2f} e {:.2f} formam um triângulo com a hipotenusa {:.2f}.'.format(r2, r3, r1))
    else:
        print('As três retas ("{}","{}","{}") não formam um triângulo.'.format(r1, r2, r3))

if r2 > r1 and r2 > r3:
    if (r1 + r3) > r2:
        print('Os catetos {:.2f} e {:.2f} formam um triângulo com a hipotenusa {:.2f}.'.format(r1, r3, r2))
    else:
        print('As três retas ("{}","{}","{}") não formam um triângulo.'.format(r1, r2, r3))

if r3 > r2 and r3 > r1:
    if (r2 + r1) > r3:
        print('Os catetos {:.2f} e {:.2f} formam um triângulo com a hipotenusa {:.2f}.'.format(r2, r1, r3))
    else:
        print('As três retas ("{}","{}","{}") não formam um triângulo.'.format(r1, r2, r3))
