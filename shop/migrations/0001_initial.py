# Generated by Django 4.0.4 on 2022-05-05 07:18

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
                ('title', models.CharField(max_length=70, verbose_name='Название')),
                ('image', models.ImageField(upload_to='images', verbose_name='Изображение')),
                ('country', models.CharField(max_length=70, verbose_name='Регион')),
                ('description', models.TextField(verbose_name='Описание')),
                ('address', models.TextField(blank=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ['title'],
            },
        ),
    ]