from MeuCursoEmVídeo.ex115.lib.interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um erro na criação do arquivo\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mHouve um erro na leitura do arquivo.\033[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<33}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome= 'desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mHouve um erro na abertura do arquivo.\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um erro na hora de escrever os dados.\033[m')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()