# Generated by Django 3.2 on 2022-12-07 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100, verbose_name='Название Бренда')),
                ('brand_description', models.TextField(max_length=200, verbose_name='Описание')),
                ('brand_slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('category_description', models.TextField(max_length=200, verbose_name='Описание')),
                ('category_slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes_name', models.CharField(max_length=100, verbose_name='Название')),
                ('clothes_description', models.TextField(max_length=200, verbose_name='Описание')),
                ('clothes_slug', models.SlugField(max_length=100, unique=True)),
                ('clothes_type', models.CharField(choices=[('man', 'Мужской'), ('woman', 'Женский'), ('kid', 'Детский'), ('uni', 'Универсальный')], max_length=10)),
                ('clothes_season', models.CharField(choices=[('winter', 'Зима'), ('spring', 'Весна'), ('summer', 'Лето'), ('autumn', 'Осень')], max_length=10, verbose_name='Сезон')),
                ('clothes_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('clothes_image', models.ImageField(upload_to='clothes', verbose_name=' Изобрежение')),
                ('clothes_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes', to='main.brand')),
                ('clothes_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes', to='main.category')),
            ],
        ),
    ]