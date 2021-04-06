n = int(input('Quantos números da sequência de Fibonacci queres ver? '))
f1 = f2 = fn = 1
cont = 3
print('{} -> {} -> '.format(0, 1), end='')
while cont <= n and n > 0:
    print('{} -> '.format(fn), end='')
    fn = f1 + f2
    f1 = f2
    f2 = fn
    cont += 1
print('FIM')
