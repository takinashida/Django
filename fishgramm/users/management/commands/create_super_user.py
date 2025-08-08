from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(email="admin@example.com")
        user.set_password("86427531")
        user.is_staff=True
        user.is_superuser=True
        user.save()
        if created:
            self.stdout.write(self.style.SUCCESS(f'Successfully added new superuser: {user.email}'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser already exist: {user.email}'))



