from django.core.management import BaseCommand

from for_hw192.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'product_name': 'продукт111', 'category': 'окна'},
            {'product_name': 'продукт112', 'category': 'двери'},
            {'product_name': 'продукт113', 'category': 'окна'},
            {'product_name': 'продукт114', 'category': 'окна'},
        ]

        Product.objects.all().delete()

        res = []
        for i in product_list:
            res.append(Product(**i))
        Product.objects.bulk_create(res) #функция для пакетного добавления