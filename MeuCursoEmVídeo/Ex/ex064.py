n = 0
cont = 0
soma = 0
print('-'*15)
print('VAMOS SOMAR!!')
print('-'*15)
while n != 999:
    n = int(input('Digite um número inteiro ou "999" para parar: '))
    if n != 999:
        cont += 1
        soma += n
print('~'*15)
print('Foram digitados {} números e a soma deles é: {}.'.format(cont, soma))
print('~'*15)
print('FIM')