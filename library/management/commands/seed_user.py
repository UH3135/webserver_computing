from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker


class Command(BaseCommand):
    def handle(self, *arg, **kargs):
        fake = Faker()
        for i in range(5):
            User.objects.create(
                username=fake.name(),
                password=fake.pyint(min_value=8, max_value=16)
            )
