from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
    
	path('admin/', admin.site.urls),
    
	path('utilizadores/', views.UtilizadorListView.as_view(), name='utilizador_list'),
	path('utilizadores/add/', views.UtilizadorCreateView.as_view(), name='utilizador_create'),
	path('utilizadores/<int:pk>/', views.UtilizadorDetailView.as_view(), name='utilizador_detail'),
    path('utilizadores/<int:pk>/delete/', views.UtilizadorDeleteView.as_view(), name='utilizador_delete'),
	path('utilizadores/<int:pk>/edit/', views.UtilizadorUpdateView.as_view(), name='utilizador_edit'),
    
	path('playlists/', views.PlaylistListView.as_view(), name='playlist_list'),
	path('playlists/add/', views.PlaylistCreateView.as_view(), name='playlist_create'),
	path('playlists/<int:pk>/', views.PlaylistDetailView.as_view(), name='playlist_detail'),
    path('playlists/<int:pk>/delete/', views.PlaylistDeleteView.as_view(), name='playlist_delete'),
	path('playlists/<int:pk>/edit/', views.PlaylistUpdateView.as_view(), name='playlist_edit'),
    path('playlists/<int:pk>/modify/', views.PlaylistModifyView.as_view(), name='playlist_modify'),
    
	path('artistas/', views.ArtistaListView.as_view(), name='artista_list'),
	path('artistas/add/', views.ArtistaCreateView.as_view(), name='artista_create'),
	path('artistas/<int:pk>/', views.ArtistaDetailView.as_view(), name='artista_detail'),
    path('artistas/<int:pk>/delete/', views.ArtistaDeleteView.as_view(), name='artista_delete'),
	path('artistas/<int:pk>/edit/', views.ArtistaUpdateView.as_view(), name='artista_edit'), 
    
	path('albuns/', views.AlbumListView.as_view(), name='album_list'),
	path('albuns/add/', views.AlbumCreateView.as_view(), name='album_create'),
	path('albuns/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('albuns/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album_delete'),
	path('albuns/<int:pk>/edit/', views.AlbumUpdateView.as_view(), name='album_edit'),
    
    path('musicas/', views.MusicaEstatisticaListView.as_view(), name='musicaestatistica_list'),
	path('musicas/add/', views.MusicaEstatisticaCreateView.as_view(), name='musicaestatistica_create'),
	path('musicas/<int:pk>/', views.MusicaEstatisticaDetailView.as_view(), name='musicaestatistica_detail'),
    path('musicas/<int:pk>/delete/', views.MusicaEstatisticaDeleteView.as_view(), name='musicaestatistica_delete'),
	path('musicas/<int:pk>/edit/', views.MusicaEstatisticaUpdateView.as_view(), name='musicaestatistica_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)