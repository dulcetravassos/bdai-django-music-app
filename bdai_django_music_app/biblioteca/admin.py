from django.contrib import admin
from .models import MusicaEstatistica, Artista, Album, Playlist, Utilizador

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
	list_display = ('nome', 'biografia')
	search_fields = ('nome',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
	list_display = ('nome', 'ano_lancamento', 'genero', 'artista')
	list_filter = ('artista',)
	search_fields = ('nome', 'ano_lancamento', 'artista__nome') # artista__nome - procura pelo nome do artista

@admin.register(Utilizador)
class UtilizadorAdmin(admin.ModelAdmin):
	list_display = ('nome_utilizador', 'email')

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
	list_display = ('nome', 'publica', 'data_criacao', 'utilizador', 'get_musicas')
	list_filter = ('publica', 'data_criacao',)
	
	filter_horizontal = ('musicas',) # widget visual
    
	def get_musicas(self, obj): # para permitir mostrar campos ManyToMany diretamente no display (uma playlist pode ter várias músicas...)
		return ", ".join([m.nome for m in obj.musicas.all()]) # transforma a lista numa string
	get_musicas.short_description = 'Músicas'

@admin.register(MusicaEstatistica)
class MusicaEstatisticaAdmin(admin.ModelAdmin):
	list_display = ('nome', 'duracao', 'url', 'estatistica_visualizacoes', 'estatistica_gostos', 'album', 'get_artistas')
	list_filter = ('album',)
	search_fields = ('nome',)

	filter_horizontal = ('artistas',)

	def get_artistas(self, obj): # para permitir mostrar campos ManyToMany diretamente no display (uma música pode ter vários artistas...)
		return ", ".join([a.nome for a in obj.artistas.all()])
	get_artistas.short_description = 'Artistas'
