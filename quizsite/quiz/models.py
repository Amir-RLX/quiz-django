from django.db import models


# Create your models here.
class Result(models.Model):
    title = models.TextField(editable=True)
    img = models.ImageField(editable=True)
    description = models.TextField(editable=True)


class Question(models.Model):
    title = models.TextField(editable=True)
    img = models.ImageField(editable=True)


class Choices(models.Model):
    ...
