# Generated by Django 4.0.4 on 2022-05-05 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='address',
        ),
        migrations.RemoveField(
            model_name='product',
            name='data',
        ),
    ]