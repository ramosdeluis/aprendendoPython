# -*- encoding: utf-8 -*-
class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome
        self.__ano = ano
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome.title()

    @property
    def ano(self):
        return self.__ano

    @property
    def likes(self):
        return self.__likes

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes}'

class Filme(Programa):
    def __init__(self,nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    @property
    def duracao(self):
        return self.__duracao

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Duração: {self.duracao} min - Likes: {self.likes}'



class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas


    @property
    def temporadas(self):
        return self.__temporadas

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self.likes}'


class Playlist:
    def __init__(self, nome, lista):
        self.__nome = nome
        self.__lista = lista

    def __getitem__(self, item):
        return self.__lista[item]

    @property
    def lista(self):
        return self.__lista

    def __len__(self):
        return len(self.__lista)

fil = Filme('fil fil', 1888, 100)
ser = Serie('ser ser', 1901, 5)
filme = Filme('filme filme', 1999, 200)
serie = Serie('serie serie', 2001, 25)
filme.dar_like()
fil.dar_like()
fil.dar_like()
fil.dar_like()
ser.dar_like()
ser.dar_like()
ser.dar_like()
ser.dar_like()
ser.dar_like()
filme.dar_like()
filme.dar_like()
filme.dar_like()
filme.dar_like()
serie.dar_like()
filme.dar_like()
# print(f'Nome: {filme.nome} - Ano: {filme.ano} - Duração: {filme.duracao} - Likes: {filme.likes}')
# print(f'Nome: {serie.nome} - Ano: {serie.ano} - Temporadas: {serie.temporadas} - Likes: {serie.likes}')
playlist_fim_de_semana = Playlist('fim de seman', [fil, filme, ser, serie])
for programa in playlist_fim_de_semana:
   # detalhes = programa.temporadas if hasattr(programa, 'temporadas') else programa.duracao
   # print(f'Nome: {programa.nome} - Detalhes: {detalhes} - Likes: {programa.likes}')
    print(programa)
print(len(playlist_fim_de_semana))