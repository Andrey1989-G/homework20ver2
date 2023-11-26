from django.db import models
from django.urls import reverse

NULLABLE = {'blank':True, 'null':True}
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')# наименование,
    descriptions = models.TextField(**NULLABLE, verbose_name='описание') # описание, можно не заполнять
    image = models.ImageField(upload_to='users_load', **NULLABLE, verbose_name='изображение') # изображение (превью),
    category = models.CharField(**NULLABLE, max_length=100, verbose_name='категория') # категория,
    price = models.IntegerField(**NULLABLE, verbose_name='цена за покупку') # цена за покупку,
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания') # дата создания,
    change_date = models.DateTimeField(**NULLABLE, auto_now=True, verbose_name='дата последнего изменения') # дата последнего изменения.

    def __str__(self):
        return f'{self.product_name} {self.category}'

    def get_absolute_url(self):
        return reverse('one_product', kwargs={'prod_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование') # наименование,
    descriptions = models.TextField(**NULLABLE, verbose_name='описание') # описание.
    # created_at = models.TextField(**NULLABLE, verbose_name='для удаления')

    def __str__(self):
        return f'{self.name}'
