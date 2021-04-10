'''
con = 0
jogador = []
jogadores = {}
totgols = 0
while True:
    print('-' * 50)
    jogador.append(str(input('Nome: ')))
    jogador.append(int(input('Número de partidas jogadas: ')))
    gols = []
    for c in range(0, jogador[1]):
        gol = int(input(f'Na {c+1}ª partida ele fez quantos gols? '))
        gols.append(gol)
        totgols += gol
    jogador.append(gols[:])
    jogador.append(totgols)
    gols.clear()
    jogadores[con] = jogador[:]
    jogador.clear()
    con += 1
    totgols = 0
    while True:
        cont = str(input('Queres continuar adicionando jogadores? [S/N] ')).strip().upper()
        if cont in 'SN':
            break
    if cont in 'N':
        break
print('-='*40)
print(f'{"COD":<4} {"Nome":<12}{"Gols":<20}{"Total"}')
print('-'*45)
for v, k in jogadores.items():
    print('{:>3}  {:<12}{}{:>20}'.format(v, k[0], k[2], k[3]))
print('-'*45)
while True:
    j = int(input('Queres ver os dados de qual jogador? '))
    if (len(jogadores)-1) >= j >= 0:
        print(f'-- Levantamento do Jogador {jogadores[j][0]}:')
        t = 1
        for k in jogadores[j][2]:
            print(f'No jogo {t} fez {k} gols.')
            t += 1
    elif j == 999:
        break
    else:
        print(f'ERRO! Não existe o jogador de código {j}. Tente novamente.')
print('-='*50)
print(f'{"FIM DO PROGRAMA":^50}')
'''
time = []
jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print('-='*30)
print(f'Foram um total de {jogador["total"]} gols.')