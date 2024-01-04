from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'google', 'category', 'create_date', 'last_edit_date')
    list_filter = ['published', 'category', 'google']


@admin.register(models.Result)
class ResultAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = [ 'title','quiz',]
    list_filter = ['quiz']


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title', 'quiz', ]
    list_filter = ['quiz']


@admin.register(models.Choices)
class ChoicesAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title','quiz', 'result', 'question')
    list_filter = ('quiz', 'result', 'question')




@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
