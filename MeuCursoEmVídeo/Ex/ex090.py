'''
aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno(a): '))
aluno['media'] = float(input('Digite a média do aluno(a): '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado!'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'de recuperação.'
else:
    aluno['situacao'] = 'reprovado...'
print('-'*30)
print(f'O nome é igual a {aluno["nome"]}.')
print(f'A média é igual a {aluno["media"]:.1f}.')
print(f'A situação é igual a {aluno["situacao"]}')
'''

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado!'
elif aluno['média'] >= 5:
    aluno['situação'] = 'de recuperação.'
else:
    aluno['situação'] = 'reprovado...'
print('-='*30)
for k, v in aluno.items():
    print(f'- {k.title()} é igual a {v}')