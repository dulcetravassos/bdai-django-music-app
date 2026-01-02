from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import MusicaEstatistica, Artista, Album, Playlist, Utilizador
from .forms import UtilizadorForm, PlaylistForm, ArtistaForm, AlbumForm, MusicaEstatisticaForm, PlaylistModifyForm
from django.db.models import Q
from django.contrib import messages

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs): # estatísticas
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

    def get_queryset(self): # Para permitir a pesquisa dinâmica
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(nome_utilizador__icontains=search_query) | # pesquisa pelo nome de utilizador
                Q(email__icontains=search_query) # pesquisa pelo email
            )
        return queryset

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

    def form_valid(self, form): # necessário para mostrar o pop-up de sucesso
        response = super().form_valid(form) # Guarda os dados primeiro
        messages.success(self.request, "Utilizador criado com sucesso!")
        return response

# Atualizar/Editar Utilizador
class UtilizadorUpdateView(UpdateView):
    model = Utilizador
    form_class = UtilizadorForm
    template_name = "utilizador_form.html"
    success_url = reverse_lazy("utilizador_list")

    def form_valid(self, form): # necessário para mostrar o pop-up de sucesso
        response = super().form_valid(form) # Guarda os dados primeiro
        messages.success(self.request, "Utilizador editado com sucesso!")
        return response

# Eliminar Utilizador
class UtilizadorDeleteView(DeleteView):
    model = Utilizador
    template_name = "utilizador_delete.html"
    success_url = reverse_lazy("utilizador_list")

    def form_valid(self, form): # necessário para mostrar o pop-up de sucesso
        response = super().form_valid(form) # Guarda os dados primeiro
        messages.success(self.request, "Utilizador eliminado com sucesso.")
        return response

################################################ Álbum ################################################

# Álbum: lista
class AlbumListView(ListView):
    model = Album
    template_name = "album_list.html"
    context_object_name = "albuns"
    ordering = ['nome']

    def get_queryset(self): # Para permitir a pesquisa dinâmica
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(nome__icontains=search_query) | # pesquisa pelo nome
                Q(artista__nome__icontains=search_query) # pesquisa pelo artista
            )
        return queryset

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

    def form_valid(self, form): # necessário para mostrar o pop-up de sucesso
        response = super().form_valid(form) # Guarda os dados primeiro
        messages.success(self.request, "Álbum adicionado com sucesso!")
        return response

# Editar Álbum
class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = "album_form.html"
    success_url = reverse_lazy("album_list")

    def form_valid(self, form): # necessário para mostrar o pop-up de sucesso
        response = super().form_valid(form) # Guarda os dados primeiro
        messages.success(self.request, "Álbum atualizado com sucesso!")
        return response

# Eliminar Álbum
class AlbumDeleteView(DeleteView):
    model = Album
    template_name = "album_delete.html"
    success_url = reverse_lazy("album_list")

    def form_valid(self, form): # necessário para mostrar o pop-up de sucesso
        response = super().form_valid(form) # Guarda os dados primeiro
        messages.success(self.request, "Álbum eliminado com sucesso.")
        return response

################################################ Artista ################################################

# Artista: lista
class ArtistaListView(ListView):
    model = Artista
    template_name = "artista_list.html"
    context_object_name = "artistas"
    ordering = ['nome']

    def get_queryset(self): # Para permitir a pesquisa dinâmica
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(nome__icontains=search_query)
        return queryset

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

    def form_valid(self, form): # necessário para mostrar o pop-up de sucesso
        response = super().form_valid(form) # Guarda os dados primeiro
        messages.success(self.request, "Artista adicionado com sucesso!")
        return response

# Editar Artista
class ArtistaUpdateView(UpdateView):
    model = Artista
    form_class = ArtistaForm
    template_name = "artista_form.html"
    success_url = reverse_lazy("artista_list")

    def form_valid(self, form): # necessário para mostrar o pop-up de sucesso
        response = super().form_valid(form) # Guarda os dados primeiro
        messages.success(self.request, "Artista atualizado com sucesso!")
        return response

# Eliminar Artista
class ArtistaDeleteView(DeleteView):
    model = Artista
    template_name = "artista_delete.html"
    success_url = reverse_lazy("artista_list")

    def form_valid(self, form): # necessário para mostrar o pop-up de sucesso
        response = super().form_valid(form) # Guarda os dados primeiro
        messages.success(self.request, "Artista eliminado com sucesso.")
        return response

################################################ Playlist ################################################

# Playlist: lista
class PlaylistListView(ListView):
    model = Playlist
    template_name = "playlist_list.html"
    context_object_name = "playlists"
    ordering = ['nome']

    def get_queryset(self): # Para permitir a pesquisa dinâmica
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(nome__icontains=search_query)
        return queryset

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

    def form_valid(self, form): # necessário para mostrar o pop-up de sucesso
        response = super().form_valid(form) # Guarda os dados primeiro
        messages.success(self.request, "Playlist criada com sucesso!")
        return response

# Editar Playlist
class PlaylistUpdateView(UpdateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = "playlist_form.html"
    success_url = reverse_lazy("playlist_list")

    def form_valid(self, form): # necessário para mostrar o pop-up de sucesso
        response = super().form_valid(form) # Guarda os dados primeiro
        messages.success(self.request, "Detalhes da playlist atualizados com sucesso!")
        return response

# Eliminar Playlist
class PlaylistDeleteView(DeleteView):
    model = Playlist
    template_name = "playlist_delete.html"
    success_url = reverse_lazy("playlist_list")

    def form_valid(self, form): # necessário para mostrar o pop-up de sucesso
        response = super().form_valid(form) # Guarda os dados primeiro
        messages.success(self.request, "Playlist eliminada com sucesso.")
        return response

# Modificar Conteúdo Playlist
class PlaylistModifyView(UpdateView):
    model = Playlist
    form_class = PlaylistModifyForm
    template_name = "playlist_modify.html"

    def get_success_url(self): # leva à playlist que acabou de ser atualizada, em vez da lista geral de todas as playlists
        return reverse('playlist_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form): # necessário para mostrar o pop-up de sucesso
        response = super().form_valid(form) # Guarda os dados primeiro
        messages.success(self.request, "Playlist atualizada com sucesso!")
        return response

################################################ Música-Estatística ################################################

# Música-Estatística: lista
class MusicaEstatisticaListView(ListView):
    model = MusicaEstatistica
    template_name = "musicaestatistica_list.html"
    context_object_name = "musicas"
    ordering = ['nome']

    def get_queryset(self): # Para permitir a pesquisa dinâmica
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(nome__icontains=search_query) | # pesquisa pelo nome
                Q(artistas__nome__icontains=search_query) # pesquisa pelo artista
            )
        return queryset

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

    def form_valid(self, form): # necessário para mostrar o pop-up de sucesso
        response = super().form_valid(form) # Guarda os dados primeiro
        messages.success(self.request, "Música adicionada com sucesso!")
        return response

# Editar Música/Estatísticas
class MusicaEstatisticaUpdateView(UpdateView):
    model = MusicaEstatistica
    form_class = MusicaEstatisticaForm
    template_name = "musicaestatistica_form.html"
    success_url = reverse_lazy("musicaestatistica_list")

    def form_valid(self, form): # necessário para mostrar o pop-up de sucesso
        response = super().form_valid(form) # Guarda os dados primeiro
        messages.success(self.request, "Música atualizada com sucesso!")
        return response

# Eliminar Música e Estatísticas
class MusicaEstatisticaDeleteView(DeleteView):
    model = MusicaEstatistica
    template_name = "musicaestatistica_delete.html"
    success_url = reverse_lazy("musicaestatistica_list")

    def form_valid(self, form): # necessário para mostrar o pop-up de sucesso
        response = super().form_valid(form) # Guarda os dados primeiro
        messages.success(self.request, "Música eliminada com sucesso.")
        return response