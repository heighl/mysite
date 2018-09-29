from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class AdminQuestion(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    inlines = [ChoiceInline]


admin.site.register(Question, AdminQuestion)
