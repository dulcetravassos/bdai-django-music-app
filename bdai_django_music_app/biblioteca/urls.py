from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('utilizadores/', views.utilizador_list, name='utilizador_list'),
	path('utilizadores/add/', views.utilizador_create, name='utilizador_create'),
	path('utilizadores/<int:pk>/', views.utilizador_detail, name='utilizador_detail'),
    path('playlists/', views.playlist_list, name='playlist_list'),
	path('playlists/add/', views.playlist_create, name='playlist_create'),
	path('playlists/<int:pk>/', views.playlist_detail, name='playlist_detail'),
    path('artistas/', views.artista_list, name='artista_list'),
	path('artistas/add/', views.artista_create, name='artista_create'),
	path('artistas/<int:pk>/', views.artista_detail, name='artista_detail'),
    path('albuns/', views.album_list, name='album_list'),
	path('albuns/add/', views.album_create, name='album_create'),
	path('albuns/<int:pk>/', views.album_detail, name='album_detail'),
    path('musicas/', views.musicaestatistica_list, name='musicaestatistica_list'),
	path('musicas/add/', views.musicaestatistica_create, name='musicaestatistica_create'),
	path('musicas/<int:pk>/', views.musicaestatistica_detail, name='musicaestatistica_detail'),
]
