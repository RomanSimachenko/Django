# Generated by Django 4.0.2 on 2022-04-09 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('full_name', models.CharField(max_length=300, unique=True, verbose_name='Full name')),
                ('total', models.PositiveIntegerField(verbose_name='Total')),
                ('correct', models.PositiveIntegerField(verbose_name='Correct')),
                ('wrong', models.PositiveIntegerField(verbose_name='Wrong')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.CharField(max_length=1000, verbose_name='Ask')),
                ('answer1', models.CharField(max_length=1000, verbose_name='Answer1')),
                ('answer2', models.CharField(max_length=1000, verbose_name='Answer2')),
                ('answer3', models.CharField(max_length=1000, verbose_name='Answer3')),
                ('answer4', models.CharField(max_length=1000, verbose_name='Answer4')),
                ('right_answer', models.PositiveIntegerField(help_text='Type number of the right answer', verbose_name='Right answer')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('answers', models.ManyToManyField(to='quiz_app.Answer', verbose_name='Answers')),
                ('questions', models.ManyToManyField(to='quiz_app.Question', verbose_name='Questions')),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizs',
            },
        ),
    ]