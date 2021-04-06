mediaIdade = 0
hMaisVelho = ''
idadeDoMaisVelho = 0
mMenoresDeVinte = 0
for c in range(1, 5):
    nome = str(input('Qual o nome da {}ª pessoa? '.format(c)))
    idade = int(input('Qual a idade da {}ª pessoa? '.format(c)))
    sexo = int(input('Digite [1] para Masculino e [2] para feminino.'))

    mediaIdade += idade
    if sexo == 1:
        if hMaisVelho == '':
            hMaisVelho = nome
            idadeDoMaisVelho = idade
        elif idadeDoMaisVelho < idade:
            hMaisVelho = nome
            idadeDoMaisVelho = idade
    elif sexo == 2 and idade <20:
            mMenoresDeVinte += 1
    else:
        print('Opção inválidade, reinicie o programa.')

print('''
A média de idades é: \033[34m{:.1f}\033[m
O homem mais velho se chama: \033[34m{}\033[m
O número de mulheres menores de 20 é \033[34m{:.0f}\033[m'''.format(mediaIdade/4, hMaisVelho, mMenoresDeVinte))