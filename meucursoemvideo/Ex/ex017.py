#co = float(input('Qual o cateto oposto? '))
#ca = float(input('Qual o cateto adjacente? '))
#h = ((co)**2+(ca)**2)**(1/2)
#print('A hipotenusa mede: {:.2f} m'.format(h))

import math

co = float(input('Qual o cateto oposto? '))
ca = float(input('Qual o cateto adjacente? '))
h = math.hypot(ca, co)
print('A hipotenusa é {}'.format(h))
