# Generated by Django 5.0 on 2023-12-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='questions',
            new_name='quiz',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='status',
            new_name='published',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='results',
            new_name='quiz',
        ),
        migrations.AddField(
            model_name='quiz',
            name='not_published',
            field=models.BooleanField(default=False, verbose_name='NOT Published'),
        ),
    ]
