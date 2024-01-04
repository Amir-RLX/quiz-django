# Generated by Django 5.0 on 2024-01-03 09:59

import django.db.models.deletion
import quiz.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_edit_date', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
                ('google', models.BooleanField(default=False, verbose_name='Google')),
                ('quiz_img', models.ImageField(blank=True, null=True, upload_to=quiz.models._get_file_name)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='quiz.category')),
            ],
            options={
                'ordering': ['create_date'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('question_img', models.ImageField(blank=True, null=True, upload_to=quiz.models._get_file_name)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quiz.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('result_img', models.ImageField(blank=True, null=True, upload_to=quiz.models._get_file_name)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quiz.quiz')),
            ],
            options={
                'ordering': ['quiz'],
            },
        ),
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quiz.question')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quiz.quiz')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quiz.result')),
            ],
        ),
    ]
