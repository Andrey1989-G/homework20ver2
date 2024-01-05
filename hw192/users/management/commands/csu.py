from django.core.management import BaseCommand

from users.models import User


#из-за того что мы поменяли настройки команда крейтсуперюзер отвалилась,
# делаем кастомную команду
class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin',
            first_name='Admin',
            last_name='adminski',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('0551')
        user.save()
