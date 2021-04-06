t = int(input('Digite um termo: '))
r = int(input('Digite uma razão: '))
cont = 1
d = 'Ss'
while cont < 11:
    print('{} -> '.format(t), end='')
    t += r
    cont += 1

print('Fim...')