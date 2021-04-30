'''nums = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', \
       'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quize', \
       'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    num = int(input('Digite um número de 0 a 20: '))
    while True:
        if num not in range(0, 21):
            num = int(input('Número inválido, digite outro número: '))
        else:
            print(f'Tu digitaste {nums[num]}.')
            break
    cont = str(input('Queres continuar? [S/N] ')).strip().upper()[0]
    num = 0
    if cont in 'N':
        break
print('~'*30)
print('{:^30}'.format('Fim do Programa.'))
print('~'*30)'''

nums = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', \
       'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quize', \
       'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    while True:
        num = int(input('Digite um valor entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Número inválido.', end=' ')
    print(f'Tu digitaste {nums[num]}.')
    while True:
        d = str(input('Queres continuar? [S/N] ')).strip().upper()[0]
        if d in 'SN':
            break
    if d in 'N':
        break
print('~'*30)
print('{:^30}'.format('Fim do Programa.'))
print('~'*30)