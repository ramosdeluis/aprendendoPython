""" CONSEGUIIIII. Agora vou fazer como na resolução.
f = str(input('''Digite uma frase e descubra se ela é um \033[34mPalíndromo\033[m:
''')).upper().strip().split()
s = ''.join(f)
t = 0
for c in range(0, len(s)):
    if s[c] == s[(len(s)-c-1)]:
        t += 1

if t == len(s):
    print('É palíndromo!')
else:
    print('Não é palíndromo...')"""

f = str(input('''Digite uma frase e descubra se ela é um \033[34mPalíndromo\033[m:
''')).upper().strip().split()
junto = ''.join(f)
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('{} é um \033[34mPalíndromo\033[m!'.format(junto))
else:
    print('{} não é um \033[34mPalíndromo\033[m...'.format(junto))
