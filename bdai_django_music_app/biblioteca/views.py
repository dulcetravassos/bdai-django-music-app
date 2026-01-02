from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import MusicaEstatistica, Artista, Album, Playlist, Utilizador
from .forms import UtilizadorForm, PlaylistForm, ArtistaForm, AlbumForm, MusicaEstatisticaForm, PlaylistModifyForm

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_utilizadores'] = Utilizador.objects.count()
        context['num_playlists'] = Playlist.objects.count()
        context['num_artistas'] = Artista.objects.count()
        context['num_albuns'] = Album.objects.count()
        context['num_musicas'] = MusicaEstatistica.objects.count()
        return context

################################################ Utilizador ################################################

# Utilizador: lista
class UtilizadorListView(ListView):
    model = Utilizador
    template_name = "utilizador_list.html"
    context_object_name = "utilizadores"
    ordering = ['nome_utilizador']

# Utilizador: detalhes + playlists
class UtilizadorDetailView(DetailView):
    model = Utilizador
    template_name = "utilizador_detail.html"
    context_object_name = "utilizador"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = self.object.playlists.all()
        return context

# Adicionar Utilizador
class UtilizadorCreateView(CreateView):
    model = Utilizador
    form_class = UtilizadorForm
    template_name = "utilizador_form.html"
    success_url = reverse_lazy("utilizador_list")

# Atualizar/Editar Utilizador
class UtilizadorUpdateView(UpdateView):
    model = Utilizador
    form_class = UtilizadorForm
    template_name = "utilizador_form.html"
    success_url = reverse_lazy("utilizador_list")

# Eliminar Utilizador
class UtilizadorDeleteView(DeleteView):
    model = Utilizador
    template_name = "utilizador_delete.html"
    success_url = reverse_lazy("utilizador_list")

################################################ Álbum ################################################

# Álbum: lista
class AlbumListView(ListView):
    model = Album
    template_name = "album_list.html"
    context_object_name = "albuns"
    ordering = ['nome']

# Álbum: detalhes (inclui artista) + músicas
class AlbumDetailView(DetailView):
    model = Album
    template_name = "album_detail.html"
    context_object_name = "album"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["musicas"] = self.object.musicas_estatisticas.all()
        return context

# Adicionar Álbum
class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = "album_form.html"
    success_url = reverse_lazy("album_list")

# Editar Álbum
class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = "album_form.html"
    success_url = reverse_lazy("album_list")

# Eliminar Álbum
class AlbumDeleteView(DeleteView):
    model = Album
    template_name = "album_delete.html"
    success_url = reverse_lazy("album_list")

################################################ Artista ################################################

# Artista: lista
class ArtistaListView(ListView):
    model = Artista
    template_name = "artista_list.html"
    context_object_name = "artistas"
    ordering = ['nome']

# Artista: detalhes + músicas + álbuns
class ArtistaDetailView(DetailView):
    model = Artista
    template_name = "artista_detail.html"
    context_object_name = "artista"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["musicas"] = self.object.musicas_estatisticas.all()
        context["albuns"] = self.object.albuns.all()
        return context

# Adicionar Artista
class ArtistaCreateView(CreateView):
    model = Artista
    form_class = ArtistaForm
    template_name = "artista_form.html"
    success_url = reverse_lazy("artista_list")

# Editar Artista
class ArtistaUpdateView(UpdateView):
    model = Artista
    form_class = ArtistaForm
    template_name = "artista_form.html"
    success_url = reverse_lazy("artista_list")

# Eliminar Artista
class ArtistaDeleteView(DeleteView):
    model = Artista
    template_name = "artista_delete.html"
    success_url = reverse_lazy("artista_list")

################################################ Playlist ################################################

# Playlist: lista
class PlaylistListView(ListView):
    model = Playlist
    template_name = "playlist_list.html"
    context_object_name = "playlists"
    ordering = ['nome']

# Playlist: detalhes
class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = "playlist_detail.html"
    context_object_name = "playlist"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["musicas"] = self.object.musicas.all()
        return context

# Adicionar Playlist
class PlaylistCreateView(CreateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = "playlist_form.html"
    success_url = reverse_lazy("playlist_list")

# Editar Playlist
class PlaylistUpdateView(UpdateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = "playlist_form.html"
    success_url = reverse_lazy("playlist_list")

# Eliminar Playlist
class PlaylistDeleteView(DeleteView):
    model = Playlist
    template_name = "playlist_delete.html"
    success_url = reverse_lazy("playlist_list")

# Modificar Conteúdo Playlist
class PlaylistModifyView(UpdateView):
    model = Playlist
    form_class = PlaylistModifyForm
    template_name = "playlist_modify.html"
    def get_success_url(self): # leva à playlist que acabou de ser atualizada, em vez da lista geral de todas as playlists
        return reverse('playlist_detail', kwargs={'pk': self.object.pk})

################################################ Música-Estatística ################################################

# Música-Estatística: lista
class MusicaEstatisticaListView(ListView):
    model = MusicaEstatistica
    template_name = "musicaestatistica_list.html"
    context_object_name = "musicas"
    ordering = ['nome']

# Música-Estatística: detalhes
class MusicaEstatisticaDetailView(DetailView):
    model = MusicaEstatistica
    template_name = "musicaestatistica_detail.html"
    context_object_name = "musicaestatistica"

# Adicionar Música-Estatística
class MusicaEstatisticaCreateView(CreateView):
    model = MusicaEstatistica
    form_class = MusicaEstatisticaForm
    template_name = "musicaestatistica_form.html"
    success_url = reverse_lazy("musicaestatistica_list")

# Editar Música/Estatísticas
class MusicaEstatisticaUpdateView(UpdateView):
    model = MusicaEstatistica
    form_class = MusicaEstatisticaForm
    template_name = "musicaestatistica_form.html"
    success_url = reverse_lazy("musicaestatistica_list")

# Eliminar Música e Estatísticas
class MusicaEstatisticaDeleteView(DeleteView):
    model = MusicaEstatistica
    template_name = "musicaestatistica_delete.html"
    success_url = reverse_lazy("musicaestatistica_list")