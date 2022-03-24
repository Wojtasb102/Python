import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    ANSWER_TYPES = [
        ('Pole Tekstowe', 'Text Field'),
        ('Pojedynczego wybory', 'Singlechoice'),
        ('Wielokrotnego wyboru', 'Multiplechoice'),
        ('Skala', 'Scale')
    ]
    answer_type = models.CharField(max_length=30, choices=ANSWER_TYPES, default="Pole Tekstowe")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return ("Odpowiedź: {} ".format(self.choice_text))


class Answer(models.Model):
    user = models.CharField(max_length=30)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question")
    answer = models.CharField(max_length=200)


