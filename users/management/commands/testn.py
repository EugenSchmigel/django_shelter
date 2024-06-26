from django.core.management import BaseCommand

from users.services import MyBot


class Command(BaseCommand):
    def handle(self, *args, **options):
        my_bot = MyBot()
        my_bot.send_message('Hi')