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
    print('Reprovado! A média é 5, faltaram {:.1f} pontos para a recuperação.'.format(5-m))
elif 7 > m >= 5:
    print('De Recuperação! A tua média foi de {:.1f}'.format(m))
else:
    print('Parabéns, aprovado com média {:.1f}'.format(m))
