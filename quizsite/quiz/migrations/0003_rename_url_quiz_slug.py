# Generated by Django 5.0 on 2024-01-03 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quiz_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='url',
            new_name='slug',
        ),
    ]
