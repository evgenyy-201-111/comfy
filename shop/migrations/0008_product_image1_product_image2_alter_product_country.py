# Generated by Django 4.0.4 on 2022-05-07 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_description_actual_alter_product_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(default=1, upload_to='images', verbose_name='Изображение '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default=1, upload_to='images', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='country',
            field=models.CharField(max_length=190, verbose_name='Заявитель'),
        ),
    ]