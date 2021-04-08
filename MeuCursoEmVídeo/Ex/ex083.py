''' O meu teve um bug... não funciona se a ordem for invertida = )a+b(
lista = []
aber = 0
fec = 0
ex = str(input('Digite uma expressão qualquer: '))
for c in ex:
    if c in '(':
        aber += 1
    elif c in ')':

        fec +=1
if aber == fec:
    print('Essa expressão é \033[34mválida\033[m!')
else:
    print('Essa expressão é \033[31minválida\033[m...')
'''

ex = str(input('Digite um valor: '))
pilha = []
for simb in ex:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada...')