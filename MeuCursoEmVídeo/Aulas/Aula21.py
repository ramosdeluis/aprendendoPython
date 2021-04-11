# Interactive Help
#help() #Comando que expica tudo
#print(input.__doc__) #Mesma coisa só que não interativo


# docstrings / Um manual do que faz a função
#def contador(i, f, p):
#    """
#    -> Faz uma contagem e mostra na tela.
#    :param i: início da contagem
#    :param f: fim da contagem
#    :param p: passo da contagem
#    :return: sem retorno
#    """
#    con = i
#    while con <= f:
#        print(f'{con}', end=' ')
#       con += p
#    print('FIM!')
#help(contador)


# Argumentos opcionais
#def somar(a=0, b=0, c=0):
#   """
#    -> Faz a soma de três valores.
#    :param a: o primeiro valor
#    :param b: o segundo valor
#    :param c: o terceiro valor
#    """
#    s = a + b + c
#    print(f'{s}')
#somar(3, 4, 8)


# Escopo de variáveis
# Declarações dentro de funções só funcionam nas mesmas
# Se declarar uma variável com o mesmo nome de uma global dentro da
# função irá criar uma local com o mesmo nome
# global a faz não criar uma local de a e usar a global dentro da função


# Retorno de resultados
# return s

#def fatorial(num=1):
#    f = 1
#    for c in range(num, 0, -1):
#        f *= c
#    return f
#n = int(input('Digite um número: '))
#print(f'O fatorial de {n} é igaul a {fatorial(n)}')
#print(f'Os fatoriais são: ')
#print(f'{fatorial(n-1)}', end=' ')
#print(f'{fatorial(n)}', end=' ')
#print(f'{fatorial(n+1)}', end=' ')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Número: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')