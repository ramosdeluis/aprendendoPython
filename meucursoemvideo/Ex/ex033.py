a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))

menor = maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print('O menor é {:.2f}.'.format(menor))
print('O maior é {:.2f}'.format(maior))
