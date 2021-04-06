#Aula de Laços de repetição: while.

'''for c in range(1, 11):
    print(c)
print('Fim da Contagem')
c = 1'''

'''while c <= 10:
    print(c)
    c += 1
print('Fim da Contagem')
'''
'''
r = 'S'
while r in 'Ss':
    c = int(input('Digite um valor: '))
    r = str(input('Queres continuar? [S/N] '))
print('Fim')
'''
n = 1
par = -1
impar = 0
print('Digite 0 para parar.')
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Vocês digitou {} números pares e {} ímpares.'.format(par, impar))
