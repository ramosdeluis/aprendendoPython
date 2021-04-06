s = 0
ns = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        ns += 1
print('A soma de todos os {} números ímpares, de 1 a 500, que são multiplos de três é: {}'.format(ns,s))
