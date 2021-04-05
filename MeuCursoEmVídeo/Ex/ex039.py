print('=-='*11)
print('{}'.format('Calculo do alistamento militar...'))
print('=-='*11)
sexo = int(input('''Qual o teu sexo?
[1] - Masculino
[2] - Feminino
'''))
if sexo == 1:
    alistou = int(input('''Tu já te apresentaste no exército?
[1] - Sim
[2] - Não
'''))
    if alistou == 1:
        print('Ok, tudo certo então. Sem problemas legais.')
    elif alistou == 2:
        idade = int(input('''Qual a tua idade?
'''))
        if idade == 18:
            print('Está no ano do alistamento, compareça ao exército.')
        elif idade < 18:
            print('Só com 18 o alistamento obrigatório, faltam {} anos.'.format(18-idade))
        else:
            print('Estás atrasado com o alistamento. Deverias ter '
                  'comparecido com 18. {} anos atrasado.'.format(idade-18))
    else:
        print('Opção inválida, reinicie o programa.')
elif sexo == 2:
    print('Mulheres não precisam se apresentar obrigatoriamente ao exército.')
else:
    print('Opção inválida, reinicie o programa.')
