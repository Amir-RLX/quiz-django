from django.db import models
import uuid


# Create your models here.
class Quiz(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    title = models.TextField(editable=True)
    img = models.ImageField(editable=True)
    results = models.ForeignKey('Result', on_delete=models.PROTECT)
    questions = models.ForeignKey('Question', on_delete=models.PROTECT)


class Result(models.Model):
    title = models.TextField(editable=True)
    img = models.ImageField(editable=True)
    description = models.TextField(editable=True)


class Question(models.Model):
    title = models.TextField(editable=True)
    img = models.ImageField(editable=True)


class Choices(models.Model):
    title = models.TextField(editable=True)
    question = models.ForeignKey('Question', on_delete=models.PROTECT)
    result = models.ForeignKey('Result', on_delete=models.PROTECT)
