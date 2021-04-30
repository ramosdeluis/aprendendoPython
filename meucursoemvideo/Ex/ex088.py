from random import randint
from time import sleep
print('-'*40)
print(f'{"JOGO DA MEGA SENA":^40}')
print('-'*40)
pal = []
lis = []
p = int(input('Quantos palpites tu queres gerar? '))
for c in range(0, p):
    for d in range(0, 6):
        lis.append(randint(1, 60))
    pal.append(lis[:])
    lis.clear()
print('-='*4 + f'  {f"SORTEADO {p} JOGOS"}  ' + '=-'*4)
sleep(1)
for c in range(0, p):
    print(f'Jogo {c+1}: {pal[c]}', end='\n')
    sleep(0.8)
print('-='*6 +f' {"BOA SORTE!"} '+ '=-'*6)
