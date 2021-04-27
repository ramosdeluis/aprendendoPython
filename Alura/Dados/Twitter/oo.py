import pprint

import oauth2
import json
import urllib.parse


class Requisição:
    def __init__(self):
        self.cliente = self.gera_cliente()

    def cria_requisição(self, opção):
        if opção == '1':
            return Posta(self.cliente)
        elif opção == '2':
            return Pesquisa(self.cliente)

    def gera_cliente(self):
        api_key = ''
        api_secret_key = ''
        token_key = ''
        token_secret_key = ''
        consumer = oauth2.Consumer(api_key, api_secret_key)
        token = oauth2.Token(token_key, token_secret_key)
        cliente = oauth2.Client(consumer, token)
        return cliente


class Posta:
    def __init__(self, cliente):
        self.cliente = cliente
        self.texto = self.solicita_texto()
        self.requisita(self.texto)

    def solicita_texto(self):
        query = input('O que queres postar, @luisraamons? ')
        query_codificado = urllib.parse.quote(query, safe='')
        return query_codificado

    def requisita(self, query_codificado):
        requisicao = self.cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificado,
                                          method='POST')
        return requisicao

class Pesquisa:
    def __init__(self, cliente):
        self.cliente = cliente
        self.objeto = self.requisita(self.solicita_texto())

    def solicita_texto(self):
        query = input('O que queres pesquisar no Twitter? ')
        query_codificado = urllib.parse.quote(query, safe='')
        return query_codificado

    def requisita(self, query_codificado):
        requisicao = self.cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificado + '&lang=pt')
        decodificado = requisicao[1].decode()
        objeto = json.loads(decodificado)
        return objeto

    def formata(self):
        twittes = self.objeto['statuses']
        for twit in twittes:
            print(f'{"-*-"*30}\nO usuário \033[34m@{twit["user"]["screen_name"]}\033[m diz:\n\033[31m{twit["text"]}\033[m')