maiores = 0
homens = 0
mulheres20 = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    while True:
        idade = int(input('Idade: '))
        while True:
            sexo = str(input('Sexo [M/F]: '))
            if sexo in 'mMfF':
                break
        if idade >= 18:
            maiores += 1
        if sexo in 'Mm':
            homens += 1
        if sexo in 'Ff' and idade < 20:
            mulheres20 += 1
        break
    while True:
        cont = str(input('Queres continuar? [S/N] '))
        if cont in 'SsNn':
            break
    if cont in 'Nn':
        break
print('-'*30)
print(f'Dessas pessoas, \033[32m{maiores}\033[m são maiores de idade, '
      f'\033[33m{homens}\033[m são homens e \033[34m{mulheres20}\033[m são mulheres menores de 20 anos.')
