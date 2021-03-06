# Generated by Django 4.0.4 on 2022-05-07 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_product_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_actual',
            field=models.TextField(default=1, verbose_name='Актуальность'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='country',
            field=models.CharField(max_length=190, verbose_name='Регион'),
        ),
    ]
