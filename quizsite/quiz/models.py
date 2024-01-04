from django.db import models
import uuid
import os
from django.utils import timezone


# Create your models here.
def _get_file_name(obj, file):
    name = uuid.uuid4()
    ext = os.path.splitext(file)[1].lower()
    path = timezone.now().strftime('images/%Y/%m/%d/')
    return os.path.join(path, f'{name}{ext}')


class Quiz(models.Model):
    class Meta:
        ordering = ['create_date']
    slug = models.SlugField(max_length=255, null=True, blank=True)
    title = models.TextField(editable=True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_edit_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(verbose_name="Published", default=False)
    google = models.BooleanField(verbose_name="Google", default=False)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.PROTECT)
    quiz_img = models.ImageField(upload_to=_get_file_name, editable=True, null=True, blank=True)

    def __str__(self):
        return self.title


class Result(models.Model):
    class Meta:
        ordering = ['quiz']

    title = models.TextField(editable=True)
    description = models.TextField(editable=True)
    quiz = models.ForeignKey('Quiz', on_delete=models.PROTECT)
    result_img = models.ImageField(upload_to=_get_file_name, editable=True, null=True, blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.TextField(editable=True)
    quiz = models.ForeignKey('Quiz', on_delete=models.PROTECT)
    question_img = models.ImageField(upload_to=_get_file_name, editable=True, null=True, blank=True)

    def __str__(self):
        return self.title


class Choices(models.Model):
    title = models.TextField(editable=True)
    quiz = models.ForeignKey('Quiz', on_delete=models.PROTECT)
    question = models.ForeignKey('Question', on_delete=models.PROTECT)
    result = models.ForeignKey('Result', on_delete=models.PROTECT)
    select = models.BooleanField(blank=True)

    def __str__(self):
        return self.title

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.quiz != self.question.quiz:
            raise ValueError("Cannot use this quiz")

        return super().save(force_insert, force_update, using, update_fields)


class Category(models.Model):
    name = models.CharField(max_length=255)


class File(models.Model):
    text = models.TextField(editable=True)
