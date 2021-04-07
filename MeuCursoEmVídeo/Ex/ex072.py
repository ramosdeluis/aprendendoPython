nums = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', \
       'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quize', \
       'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
num = int(input('Digite um número de 0 a 20: '))
while True:
    if num not in range(0, 11):
        num = int(input('Número inválido, digite outro número: '))
    if 0 <= num <= 20:
        print(f'Tu digitaste {nums[num]}.')
        break


print('~'*30)
print('{:^30}'.format('Fim do Programa.'))