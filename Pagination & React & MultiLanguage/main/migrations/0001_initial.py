# Generated by Django 4.0.3 on 2022-03-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('price', models.PositiveIntegerField(help_text='indicate price in USD($)', verbose_name='Price')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
