''' Consegui, agora vou tentar como está no vídeo.
t = int(input('Digite um termo: '))
r = int(input('Digite uma razão: '))
cont = 1
d = 'Ss'
mostrados = 0
novos = 11
while d in 'Ss' and novos != 1:
    mostrados += novos - 1
    while cont < novos:
        print('{} -> '.format(t), end='')
        t += r
        cont += 1
    print('PAUSA')
    d = str(input('Queres mostrar novos termos? [S/N] '))
    if d in 'Ss':
        novos += int(input('Quantos novos termos? ')) - cont + 1
        cont = 1
print('Foram mostrados um total de {} termos.'.format(mostrados))
print('FIM')
'''

primeiro = int(input('Digite o termo de da PA: '))
razao = int(input('Digite a razão de da PA: '))
cont = 0
termo = primeiro
mais = 10
smais = 0
while mais != 0:
    while cont < mais:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    cont = 0
    smais += mais
    mais = int(input('Mais quantas casas? '))
print('Foram mostradas {} casas.'.format(smais))
print('FIM')





























