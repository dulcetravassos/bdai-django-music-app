from django import forms
from .models import MusicaEstatistica, Artista, Album, Playlist, Utilizador

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['nome', 'ano_lancamento', 'genero', 'artista']

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nome', 'biografia']

class UtilizadorForm(forms.ModelForm):
    class Meta:
        model = Utilizador
        fields =  ['nome_utilizador', 'email', 'password']

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['nome', 'publica', 'utilizador']

class MusicaEstatisticaForm(forms.ModelForm):
    class Meta:
        model = MusicaEstatistica
        fields = ['nome', 'duracao', 'url', 'estatistica_gostos', 'estatistica_visualizacoes', 'album', 'artistas']