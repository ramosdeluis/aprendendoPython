n = int(input('Digite um número para descobrir se ele é primo: '))
s = 0
for c in range(1, n):
    if n % c == 0:
        s += 1
if s > 2:
    print('\033[34m{} não é primo!\033[m'.format(n))
else:
    print('\033[34m{} é um número primo!!\033[m'.format(n))
