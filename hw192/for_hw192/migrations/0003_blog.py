# Generated by Django 4.2.7 on 2023-12-02 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_hw192', '0002_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, null=True, verbose_name='содержимое')),
                ('img_preview', models.ImageField(blank=True, null=True, upload_to='users_load', verbose_name='изображение')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='количество просмотров')),
                ('sign_publication', models.BooleanField(default=True)),
                ('number_views', models.IntegerField(blank=True, null=True, verbose_name='цена за покупку')),
            ],
        ),
    ]
