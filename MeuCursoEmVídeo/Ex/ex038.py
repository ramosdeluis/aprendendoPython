print('=-='*9)
print('{}'.format('Vamos comparar os valores!'))
print('=-='*9)
a = int(input('Digite o primeiro valor:'))
b = int(input('Digite o segundo valor: '))

if a > b:
    print('O primeiro valor, {}, é maior do que o segundo, {}.'.format(a, b))
elif b > a:
    print('O segundo valor, {}, é maior do que o primeiro, {}.'. format(b, a))
else:
    print('Os dois valores são iguais!')
