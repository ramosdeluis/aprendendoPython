from MeuCursoEmVídeo.ex115.lib.interface import *
from MeuCursoEmVídeo.ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... até logo!')
        break
    else:
        cabeçalho('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)