from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Lists all installed apps'

    def handle(self, *args, **kwargs):
        self.stdout.write('INSTALLED_APPS:')
        for app in settings.INSTALLED_APPS:
            self.stdout.write(f'- {app}')

