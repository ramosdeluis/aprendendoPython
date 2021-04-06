continuar = 'S'
soma = 0
cont = 1
num = int(input('Digite um número: '))
continuar = str(input('Queres adicionar números? [S/N] '))
maior = menor = num
soma += num
while continuar in 'Ss':
    num = int(input('Digite um número: '))
    continuar = str(input('Queres adicionar números? [S/N] '))
    cont += 1
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print('~'*30)
print('A média entre os \033[34m{}\033[m números é de: \033[33m{:.2f}\033[m'.format(cont, soma/cont))
print('O maior foi o \033[31m{}\033[m e o menor foi \033[32m{}\033[m.'.format(maior, menor))
