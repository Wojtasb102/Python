from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Question, Choice, Answer, Profile

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(Profile)
