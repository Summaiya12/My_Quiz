from django.contrib import admin
from myapp.models import Question, Category


@admin.register(Question)
class AdminQuestion(admin.ModelAdmin):
    list_display = ['id', 'question', 'category']


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'title']
