# Generated by Django 4.0.3 on 2022-03-06 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='CategoryDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'CategoryDescription',
                'verbose_name_plural': 'CategoryDescriptions',
                'db_table': 'categorydescription',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('description', models.TextField(max_length=1000, verbose_name='Description')),
                ('amount', models.PositiveIntegerField(verbose_name='Amount')),
                ('price', models.FloatField(verbose_name='Price')),
                ('active', models.BooleanField(verbose_name='Status')),
                ('category', models.ManyToManyField(to='shops_app.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='images/shop', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Shop',
                'verbose_name_plural': 'Shops',
                'db_table': 'shop',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.ImageField(upload_to='images/product', verbose_name='Image path')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops_app.product', verbose_name='Product image')),
            ],
            options={
                'verbose_name': 'ProductImage',
                'verbose_name_plural': 'ProductImages',
                'db_table': 'product_image',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops_app.shop', verbose_name='shop'),
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.ManyToManyField(to='shops_app.categorydescription', verbose_name='Category description'),
        ),
    ]
