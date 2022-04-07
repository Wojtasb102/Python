from django.shortcuts import render

from .models import Licznik


# Create your views here.


def licznik(request, licznik_id):
    context = {
        "licznik_id": licznik_id
    }
    return render(request, "licznik.html", context)


def confirm(request, licznik_id):
    print(request.POST)
    value = request.POST.get("odczyt")
    Licznik.objects.create(licznik_id=licznik_id, value=value)
    context = {
        'value': value,
        "licznik_id": licznik_id
    }
    return render(request, "confirm.html", context)
