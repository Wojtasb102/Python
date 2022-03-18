from django.contrib import admin
from filmyweb.models import Film


# admin.site.register(Film)
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    # fields = ["tytul","opis","rok"]
    # exclude = ["opis"]
    list_display = ["tytul", "imdb_rating", "rok"]
    list_filter = ["rok"]
    search_fields = ["tytul", "opis"]
