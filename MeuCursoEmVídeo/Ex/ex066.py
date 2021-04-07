soma = 0
cont = 0
while True:
    n = int(input('Digite um número inteiro (ou 999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma entre os \033[34m{cont}\033[m números digitados é \033[32m{soma:.2f}\033[m.')