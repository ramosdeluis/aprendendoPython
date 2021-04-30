sexo = str(input('Qual o teu sexo? [M/F]: '))
while sexo not in 'MmFf':
    print('Opção inválida, digite novamente.')
    sexo = str(input('Qual o teu sexo? [M/F]: '))
print(sexo.upper())