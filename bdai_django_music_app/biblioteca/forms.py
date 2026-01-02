from django import forms
from .models import MusicaEstatistica, Artista, Album, Playlist, Utilizador

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['nome', 'capa', 'ano_lancamento', 'genero', 'artista']

    # Bloco de código para ajustar o design do form. Adaptado de:
    # https://stackoverflow.com/questions/54114635/how-can-i-add-bootstrap-styles-to-my-django-form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'
            self.fields[myField].widget.attrs['style'] = 'max-width: 400px;'

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nome', 'foto', 'biografia']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'
            self.fields[myField].widget.attrs['style'] = 'max-width: 400px;'

class UtilizadorForm(forms.ModelForm):
    class Meta:
        model = Utilizador
        fields =  ['nome_utilizador', 'email', 'password']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'
            self.fields[myField].widget.attrs['style'] = 'max-width: 400px;'

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['nome', 'publica', 'utilizador']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput): # a ticking box comporta-se de forma diferente dos restantes campos
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['style'] = 'max-width: 400px;'

class PlaylistModifyForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['musicas']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['musicas'].widget.attrs['class'] = ' select-musicas' # para poder ser referenciado no playlist_modify.html

class MusicaEstatisticaForm(forms.ModelForm):
    class Meta:
        model = MusicaEstatistica
        fields = ['nome', 'duracao', 'url', 'estatistica_gostos', 'estatistica_visualizacoes', 'album', 'artistas']
    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    for myField in self.fields:
    #        self.fields[myField].widget.attrs['class'] = 'form-control'
    #        self.fields[myField].widget.attrs['style'] = 'max-width: 400px;'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if name == 'artistas':
                field.widget.attrs['class'] += ' select-artistas' # para poder ser referenciado no musicaestatistica_form.html
            else:
                field.widget.attrs['style'] = 'max-width: 400px;'