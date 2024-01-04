from django.db import models
from django.urls import reverse

NULLABLE = {'blank':True, 'null':True}
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')# наименование,
    slug = models.SlugField(max_length=255, default="url", unique=True, db_index=True, verbose_name="URL")
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

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')# заголовок,
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(**NULLABLE, verbose_name='содержимое') # содержимое, можно не заполнять
    img_preview = models.ImageField(upload_to='users_load', **NULLABLE, verbose_name='изображение') # изображение (превью)
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='количество просмотров') # дата создания,
    sign_publication = models.BooleanField(default=True) #признак публикации
    number_views = models.IntegerField(**NULLABLE, default=0, verbose_name='просмотры') # просмотры


    def __str__(self):
        return f'{self.title}'

class Version(models.Model):
    title_version = models.CharField(max_length=100, verbose_name='название версии') # название версии,
    number_version = models.CharField(max_length=100, verbose_name='номер версии') # номер версии,
    newest_version = models.BooleanField(default=True, verbose_name='признак новейшей версии') #признак новейшей версии
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')

    def __str__(self):
        return f'{self.title_version}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'