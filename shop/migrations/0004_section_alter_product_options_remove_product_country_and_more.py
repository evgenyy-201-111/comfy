# Generated by Django 4.0.4 on 2022-05-07 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_product_address_remove_product_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Тут надо ввести название раздела', max_length=70, unique=True, verbose_name='Название раздела')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='country',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.AddField(
            model_name='product',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.section', verbose_name='Раздел'),
        ),
    ]
