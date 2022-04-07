from django.db import models

# Create your models here.

import datetime


class Licznik(models.Model):
    licznik_id = models.SmallIntegerField()
    value = models.FloatField()
    data_odczytu = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return ("Licznik nr: {} ma wartość: {} na dzień:{}".format(self.licznik_id, self.value, self.data_odczytu))
