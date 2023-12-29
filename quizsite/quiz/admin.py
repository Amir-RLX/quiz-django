from django.contrib import admin
from . import models


# Register your models here.

class QuizAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)
    list_display = ('title','published','not_published')
    search_fields = ('title',)


class ResultAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class ChoicesAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = ('quiz',)


admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.Result, ResultAdmin)
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choices, ChoicesAdmin)
