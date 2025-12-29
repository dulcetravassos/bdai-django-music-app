from django.shortcuts import render, get_object_or_404, redirect
from .models import MusicaEstatistica, Artista, Album, Playlist, Utilizador
from .forms import UtilizadorForm, PlaylistForm, ArtistaForm, AlbumForm, MusicaEstatisticaForm
from django.db.models import Prefetch

def home(request):
    return render(request, 'home.html')

################################################ Utilizador ################################################

# Utilizador: lista
def utilizador_list(request):
    utilizadores = Utilizador.objects.all()
    return render(request, 'utilizador_list.html', {'utilizadores': utilizadores})

# Utilizador: detalhes + playlists
def utilizador_detail(request, pk):
    utilizador = get_object_or_404(Utilizador, pk=pk)
    playlists = utilizador.playlists.all()
    return render(request, 'utilizador_detail.html', {'utilizador': utilizador, 'playlists': playlists})

# Adicionar Utilizador
def utilizador_create(request):
    if request.method == 'POST':
        form = UtilizadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('utilizador_list')
    else:
        form = UtilizadorForm()
    return render(request, 'utilizador_form.html', {'form': form})


################################################ Álbum ################################################

# Álbum: lista
def album_list(request):
    albuns = Album.objects.all()
    return render(request, 'album_list.html', {'albuns': albuns})

# Álbum: detalhes (inclui artista) + músicas
def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    musicas = album.musicas_estatisticas.all()
    return render(request, 'album_detail.html', {'album': album, 'musicas': musicas})

# Adicionar Álbum
def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'album_form.html', {'form': form})


################################################ Artista ################################################

# Artista: lista
def artista_list(request):
    artistas = Artista.objects.all()
    return render(request, 'artista_list.html', {'artistas': artistas})

# Artista: detalhes + músicas + álbuns
def artista_detail(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    musicas = artista.musicas_estatisticas.all()
    albuns = artista.albuns.all()
    return render(request, 'artista_detail.html', {'artista': artista, 'musicas': musicas, 'albuns': albuns})

# Adicionar Artista
def artista_create(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artista_list')
    else:
        form = ArtistaForm()
    return render(request, 'artista_form.html', {'form': form})


################################################ Playlist ################################################

# Playlist: lista
def playlist_list(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlist_list.html', {'playlists': playlists})

# Playlist: detalhes
def playlist_detail(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    musicas = playlist.musicas.all()
    return render(request, 'playlist_detail.html', {'playlist': playlist, 'musicas': musicas})

# Adicionar Playlist
def playlist_create(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('playlist_list')
    else:
        form = PlaylistForm()
    return render(request, 'playlist_form.html', {'form': form})


################################################ Música-Estatística ################################################

# Música-Estatística: lista
def musicaestatistica_list(request):
    musicaestatistica = MusicaEstatistica.objects.all()
    return render(request, 'musicaestatistica_list.html', {'musicas': musicaestatistica})

# Música-Estatística: detalhes
def musicaestatistica_detail(request, pk):
    musicaestatistica = get_object_or_404(MusicaEstatistica, pk=pk)
    return render(request, 'musicaestatistica_detail.html', {'musicaestatistica': musicaestatistica})

# Adicionar Música-Estatística
def musicaestatistica_create(request):
    if request.method == 'POST':
        form = MusicaEstatisticaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musicaestatistica_list')
    else:
        form = MusicaEstatisticaForm()
    return render(request, 'musicaestatistica_form.html', {'form': form})