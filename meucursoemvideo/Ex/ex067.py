cont = 0
while True:
    print('-'*80)
    n = float(input('Digite um número para saber a tabuada ou um número negativo para parar: '))
    if n < 0:
         break
    cont += 1
    for c in range(1, 11):
        print(f'{c} x {n:.0f} = {c * n:.0f}')
print('~'*31)
print(f'Tu perguntaste sobre \033[34m{cont}\033[m números.')
print('FIM')