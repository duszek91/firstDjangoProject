from django.contrib import admin
from .models import Question, Choice

# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date', "id"]
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'question']
    search_fields = ['choice_text']