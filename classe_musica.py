class Musica:
    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome:<20} | Artista: {self.artista:<20} | Duração: {self.duracao:>4} segundos'

    def listar_musicas():
        for musica in Musica.musicas:
            print(musica)


musica1 = Musica('Liquor Store Blues', 'Bruno Mars', 229)
musica2 = Musica('Apologize', 'OneRepublic', 184)
musica3 = Musica('Vienna', 'Billy Joel', 214)

Musica.listar_musicas()