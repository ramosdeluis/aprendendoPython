'''Estruturas Compostas, Bibliotecas.'''
'''
pessoas = {'nome': 'Luís', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
'''
'''
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} : {v}')
'''
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Digite um estado: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(f'{v}', end=' ')
    print()