from django.db import models
import uuid


# Create your models here.
class Quiz(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    title = models.TextField(editable=True)
    img = models.ImageField(editable=True, null=True, blank=True)
    published = models.BooleanField(verbose_name="Published", default=False)
    not_published = models.BooleanField(verbose_name="NOT Published", default=False)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Result(models.Model):
    title = models.TextField(editable=True)
    img = models.ImageField(editable=True, null=True, blank=True)
    description = models.TextField(editable=True)
    quiz = models.ForeignKey('Quiz', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.TextField(editable=True)
    img = models.ImageField(editable=True, null=True, blank=True)
    quiz = models.ForeignKey('Quiz', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Choices(models.Model):
    title = models.TextField(editable=True)
    quiz = models.ForeignKey('Quiz', on_delete=models.PROTECT)
    question = models.ForeignKey('Question', on_delete=models.PROTECT)
    result = models.ForeignKey('Result', on_delete=models.PROTECT)

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
