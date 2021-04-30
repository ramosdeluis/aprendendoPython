'''n = int(input('Digite um número para descobrir o seu fatorial: '))
produto = n
while n != 1:
    produto = produto * (n-1)
    n -= 1
print(produto)'''

n = int(input('Digite um número para descobrir o seu fatorial: '))
produto = n
for c in range(n, 1, -1):
    produto = produto * (c-1)
print('{}! é igual a {}.'.format(n, produto))

