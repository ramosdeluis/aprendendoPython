brasileirao = 'Palmeiras', 'Santos', 'Vasco da Gama', 'Grêmio', 'Flamengo', 'Corinthians', 'Internacional', 'Cruzeiro',\
              'São Paulo', 'Atlético Mineiro', 'Botafogo', 'Fluminense', 'Coritiba', 'Bahia', 'Goiás', 'Guarani', \
              'Sport', 'Portuguesa', 'Atlético Paranaense', 'Vitória'
print('~'*100)
print(f'Os 5 primeiro colocados são, respectivamente: {brasileirao[0]}, {brasileirao[1]}, {brasileirao[2]},'
      f' {brasileirao[3]} e {brasileirao[4]}.')
print('~'*100)
print(f'O 4 últimos colocados são: {brasileirao[-1]}, {brasileirao[-2]}, {brasileirao[-3]} e {brasileirao[-4]}')
print('~'*100)
print('Os times em ordem alfabética ficam: ')
for c in range(0, 20):
    print('{}º - {}.'.format(c+1, sorted(brasileirao)[c]))
print('~'*100)
print(f'O Inter está na {brasileirao.index("Internacional")+1}ª posição.')
print('~'*100)
