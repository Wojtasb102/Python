from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models.functions import Lower

from .models import Question, Choice, Answer, Profile

# Register your models here.
# admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(Profile)


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('question_type', 'question_number', 'answer_type')
    list_display = ('question_number', 'question_text', 'answer_type', 'choice_text')

    def get_ordering(self, request):
        return [Lower('question_number')]  # sort case insensitive


admin.site.register(Question, QuestionAdmin)
