som = 0

for c in range(0, 6):
    num = float(input('Digite um número: '))
    if num % 2 == 0:
        som += num
print('A soma dos pares é {:.2f}.'.format(som))
