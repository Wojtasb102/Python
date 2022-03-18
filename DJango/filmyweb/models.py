from django.db import models


class Film(models.Model):
    tytul = models.CharField(max_length=40, blank=False, unique=True)  # Blank = False pole musi mieć wartość
    rok = models.PositiveSmallIntegerField(default=2000)
    opis = models.TextField(default="", )
    premiera = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    plakat = models.ImageField(upload_to="plakaty", null=True, blank=True)

    def __str__(self):
        return self.tytul_z_rokiem()

    def tytul_z_rokiem(self):
        return ("{} {}".format(self.tytul, self.rok))


class Figura(models.Model):
    a = models.PositiveSmallIntegerField(blank=False)
    b = models.PositiveSmallIntegerField(blank=False)
    c = models.PositiveSmallIntegerField(blank=True,  null=True)
    rodzaj = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return ("Ta figura to {} o boku a długości {}".format(self.rodzaj, self.a))
