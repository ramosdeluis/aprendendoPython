import math
n = float(input('Digite um ângulo: '))
print('O ângulo de {:.2f} tem o seno de {:.2f}'.format(n, math.sin(math.radians(n))))
print('O ângulo de {:.2f} tem o cosseno de {:.2f}'.format(n, math.cos(math.radians(n))))
print('O ângulo de {:.2f} tem a tangente de {:.2f}'.format(n, math.tan(math.radians(n))))
