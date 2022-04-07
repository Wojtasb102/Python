from django.contrib import admin
from .models import Licznik
from django.db.models.functions import Lower

admin.site.register(Licznik)
