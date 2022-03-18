from django.urls import path
from filmyweb.views import wszystkie_filmy, nowy_film, edytuj_film, usun, wyswietl_figury, nowa_figura, add, disp_form

urlpatterns = [
    path('wszystkie/', wszystkie_filmy),
    path('nowy/', nowy_film),
    path('edytuj/<int:id>/', edytuj_film),
    path('usun/<int:id>/', usun),

    path('nowa_figura/', nowa_figura),
    path('figury/', wyswietl_figury),
    path('math/add/', add),
    path('math/',disp_form)
]
