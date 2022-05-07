from django.db import models


class Section(models.Model):
    title = models.CharField(
        max_length=70,
        help_text='Тут надо ввести название раздела',
        unique=True,
        verbose_name='Название раздела'
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=70, verbose_name='Название')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    image1 = models.ImageField(upload_to='images', verbose_name='Изображение ')
    image2 = models.ImageField(upload_to='images', verbose_name='Изображение')
    country = models.CharField(max_length=190, verbose_name='Заявитель')
    description = models.TextField(verbose_name='Описание')
    description_actual = models.TextField(verbose_name='Актуальность')

    class Meta:
        ordering = ['title']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return '{0}'.format(self.title)
