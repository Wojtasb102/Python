from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse
from .models import Film, Figura
from .forms import FilmForm, FiguraForm


# poczytac dokumentacji ORM

def wszystkie_filmy(request):
    # return HttpResponse("To jest nasz test")
    wszystkie = Film.objects.all()  # all   // get(tytul='Avatar') jestli niebyło by Avatara w bazie to zwróci błąd (trzeba robić w try except)
    # filter(tytul ='Avatar') zwraca wszystkie elementy o tej nazwie w przypadku braku to zwróc pustą tablice

    # ilosc = len(wszystkie)
    return render(request, 'filmy.html',
                  {'filmy': wszystkie})  # przekazuje zmienna filtry pod nazwa filmy do filmy.html

    # Film.objects.create(tytul= "Nowy film", rok = 2020, opis = "nowy film") tworzenie nowego rekordu

    # film = Film.objects.get(id = 2)
    # film.tytul = "nowy tytul"
    # film.save()
    # film.delete() Film.objects.get(id=2).delete()


def nowy_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form})


def edytuj_film(request, id):
    # film = Film.objects.get(id = id)
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form})


def usun(request, id):
    film = get_object_or_404(Film, pk=id)
    if request.method == "POST":
        film.delete()
        return redirect(wszystkie_filmy)
    return render(request, 'potwierdz.html', {'film': film})


def nowa_figura(request):
    print(request)
    form = FiguraForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(wyswietl_figury)
    return render(request, 'figury_form.html', {'form': form})


def wyswietl_figury(request):
    print(request)
    figury = Figura.objects.all()
    return render(request, 'figury.html', {'figury': figury})


def add(request):
    print(request)
    val1 = int(request.GET['a'])
    val2 = int(request.GET['b'])
    result = val1 + val2

    return render(request, "add_result.html", {'res': result})


def disp_form(request):
    return render(request, "add.html")