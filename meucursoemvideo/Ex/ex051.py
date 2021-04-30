'''
ter = float(input('Digite um número: '))
raz = float(input('Digite uma razão: '))
som = 0
print('Os 10 primeiros termos dessa PA são:')
for c in range(0, 10):
    print('{}'.format(ter + (c+1) * raz))
'''

ter = int(input('Digite um número: '))
raz = int(input('Digite uma razão: '))
print('Os 10 primeiros termos dessa PA são:')
for c in range(ter, ter + 10*raz, raz):
    print('{:.0f}'.format(c))
