# Generated by Django 5.0 on 2024-01-03 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='url',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
