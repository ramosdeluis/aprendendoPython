palavras = ('tapete', 'carreta', 'caderno', 'pagode', 'poeira', 'topete', 'casaco', 'esquema',
            'suspenso', 'aplauso', 'postagem', 'torpedo', 'tapume', 'excluso', 'cheiroso', 'charrete',
            'espinafre', 'esteja', 'correto', 'caroço', 'Python')
vogais = ''
print('As vogais são: ')
for pal in range(0, len(palavras)):
    for let in range(0, len(palavras[pal])):
        if palavras[pal][let].upper() in 'AEIOU':
            vogais += palavras[pal][let].upper() + ' '
    print('-'*45)
    print(f'Na palavra {palavras[pal]} temos: {vogais}')
    vogais = ''
print('-'*45)