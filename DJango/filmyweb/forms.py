from django.forms import ModelForm
from .models import Film, Figura


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['tytul', 'rok', 'premiera', 'rok', 'imdb_rating', 'plakat']


class FiguraForm(ModelForm):
    class Meta:
        model = Figura
        fields = ['a', 'b', 'c', 'rodzaj']
