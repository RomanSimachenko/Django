# Generated by Django 4.0.3 on 2022-04-11 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_options_customuser_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='about',
            field=models.CharField(max_length=500, verbose_name='About'),
        ),
    ]
