from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=512)
    biografia = models.CharField(max_length=512, blank=True, null=True)
    foto = models.ImageField(upload_to='artistas/', blank=True, null=True)

    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas' # Override standard que é o inglês

    def __str__(self):
        return f"{self.nome}"


class Utilizador(models.Model):
    nome_utilizador = models.CharField(max_length=512)
    email = models.CharField(max_length=512, unique=True)
    password = models.CharField(max_length=512)

    class Meta:
        verbose_name = 'Utilizador'
        verbose_name_plural = 'Utilizadores' # Override standard que é o inglês

    def __str__(self):
        return self.nome_utilizador
    

class Album(models.Model):
    nome = models.CharField(max_length=512)
    ano_lancamento = models.BigIntegerField()
    genero = models.CharField(max_length=512, null=True, blank=True) # opcional
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='albuns') # se o artista for eliminado, os seus álbuns são eliminados
    capa = models.ImageField(upload_to='albuns/', blank=True, null=True)

    class Meta:
        verbose_name = 'Álbum'
        verbose_name_plural = 'Álbuns' # Override standard que é o inglês

    def __str__(self):
        return f"{self.nome}, {self.artista.nome} ({self.ano_lancamento})"


class MusicaEstatistica(models.Model):
    nome = models.CharField(max_length=512)
    duracao = models.BigIntegerField()
    url = models.CharField(max_length=512, unique=True)
    estatistica_visualizacoes = models.BigIntegerField(default=0)
    estatistica_gostos = models.BigIntegerField(default=0)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musicas_estatisticas') # se o álbum for apagado, as suas músicas também são

    # Relação N:M com a tabela Artista
    artistas = models.ManyToManyField(Artista, related_name='musicas_estatisticas', db_table='artista_musica_estatistica') # Correspondência com a tabela na bd
    # Nota: apagar o artista apaga os seus álbuns que, por sua vez, apaga as suas músicas!

    class Meta:
        verbose_name = 'Música'
        verbose_name_plural = 'Músicas' # Override standard que é o inglês

    def __str__(self):
        return f"{self.nome} ({self.album.nome})"
    
    # Precisamos de uma função para alterar os urls para o django template (mas sem os modificar 
    # na base de dados), para que as músicas consigam ser reproduzidas
    def get_embed_url(self): 
        return self.url.replace("intl-pt", "embed")
    
    # Função para converter a duração de uma música de segundos para minutos (estilo xx:xx)
    def get_duracao_formatada(self):
        if self.duracao:
            minutos = self.duracao // 60
            segundos = self.duracao % 60
            return f"{minutos}:{segundos:02d}" # :02d garante que o 5 vira 05
        return "0:00"
    

class Playlist(models.Model):
    nome = models.CharField(max_length=120)
    publica = models.BooleanField()
    data_criacao = models.DateField(auto_now_add=True)
    utilizador = models.ForeignKey(Utilizador, on_delete=models.CASCADE, related_name='playlists') # apagar um utilizador, apaga as suas playlists

    # Relação M:N com a tabela Musica:
    musicas = models.ManyToManyField(MusicaEstatistica, blank=True, related_name='playlists', db_table='playlist_musica_estatistica') # Correspondência com a tabela na bd
    # Apagar uma música não apaga as playlists que a continham (desaparece apenas)!

    class Meta:
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists' # Override standard que é o inglês

    def __str__(self):
        return f"{self.nome}"

    def get_privacidade(self):
        if self.publica:
            return "Pública"
        return "Privada"