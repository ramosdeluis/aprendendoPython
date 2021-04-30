dic = {}
gols = []
dic['nome'] = str(input('Nome do jogador: '))
dic['partidas'] = int(input('Número de partidas: '))
for c in range(0, dic['partidas']):
    gols.append(int(input(f'Quantos gols goram feitos na {c+1}ª partida? ')))
dic['gols'] = gols
totalG = 0
for c in gols:
    totalG += c
dic['total'] = totalG
print('-='*35)
print(dic)
print('-='*35)
for v, k in dic.items():
    print(f'No campo {v} tem o valor {k}.')
print('-='*35)
print(f'O jogador {dic["nome"]} jogou {dic["partidas"]} partidas.')
for c in range(0, dic['partidas']):
    print(f'  => Na {c+1}ª partida, fez {dic["gols"][c]} gols.')
print('-='*30)
print(f'No total foram {dic["total"]} gols.')