import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

QUESTION_CATEGORY = (('kuchnia', 'Kuchnia'),
                     ('lazienka', 'Lazienka'),
                     ('salon', 'Salon'),
                     ('jadalnia', 'Jadalnia'),
                     ('sypialnia', 'Sypialnia'),
                     ('ogolne', 'Ogolne'))

ANSWER_TYPES = [
    ('text', 'Pole Tekstowe'),
    ('radio', 'Pojedynczego wyboru'),
    ('checkbox', 'Wielokrotnego wyboru'),
    ('Skala', 'Scale')
]


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    answer_type = models.CharField(max_length=30, choices=ANSWER_TYPES, default="Pole Tekstowe")
    question_type = models.CharField(max_length=30, choices=QUESTION_CATEGORY, default="ogolne")
    question_number = models.SmallIntegerField(default=0, blank=False)
    choice_text = models.CharField(max_length=200, default=" ", blank=True)

    def __str__(self):
        return ("{}: {}".format(self.question_number, self.question_text))

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def choice_split(self):
        return self.choice_text.split(',')

    def type(self):
        print(self.answer_type)
        return self.answer_type

    def isTextField(self):
        if self.answer_type == 'text':
            return True
        else:
            return False


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return ("{}: {} ".format(self.question, self.choice_text))

    def choice_split(self):
        return self.choice_text.split(',')


class Answer(models.Model):
    user = models.CharField(max_length=30)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question")
    answer = models.CharField(max_length=200, null=True)

    def __str__(self):
        return ("{}: {} {}".format(self.user, self.question, self.answer))

    def updates(self, answer):
        print("funkcja")
        self.answer = answer


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=100)
    my_field = MultiSelectField(choices=QUESTION_CATEGORY, default='item_key1')

    def __str__(self):
        return str(self.user)
