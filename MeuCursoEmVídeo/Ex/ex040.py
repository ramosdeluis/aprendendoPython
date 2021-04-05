print('=-='*10)
print('{}'.format('Calculo da média escolar.'))
print('=-='*10)
a = float(input('''Qual a tua primeira nota?
'''))
b = float(input('''Qual a tua segunda nota?
'''))
listaDeNotas = [a, b]

m = sum(listaDeNotas) / len(listaDeNotas)
if m < 5:
    print('Reprovado! A média é 5, faltaram {:.2f} pontos para a recuperação.'.format(5-m))
elif m >= 5 and m < 7:
    print('De Recuperação! A tua média foi de {:.2f}'.format(m))
else:
    print('Parabéns, aprovado com média {:.2f}'.format(m))
