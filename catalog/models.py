from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


def __str__(self):
    return f'{self.title} {self.price} {self.category}'


class Meta:
    verbose_name = 'Продукт'
    verbose_name_plural = 'Продукты'


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='preview/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена за покупку')
    first_data = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    last_data = models.DateTimeField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
