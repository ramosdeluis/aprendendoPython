print('=-='*10)
print('{}'.format('Calculo do alistamento militar...'))
print('=-='*10)
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
        idade = int('''Qual a tua idade? 
        ''')
        if idade == 18:
            ''
        elif idade < 18:
            ''
        else:
            print('Estás atrasado com o alistamento. Deverias ter comparecido com 18. {} anos atrasado.'.format(idade-18))
    else:
        print('Opção inválida, reinicie o programa.')
elif sexo == 2:
    print('Mulheres não precisam se apresentar obrigatoriamente ao exército.')
else:
    print('Opção inválida, reinicie o programa.')

