from django.conf import settings
from django.contrib.sites import requests
from django.core.mail import send_mail
import requests


def send_new_password(email, new_password):
    send_mail(
        subject='You have changed the password.',
        message=f'Your new password: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )


class MyBot:
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_TOKEN

    def send_message(self, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': '1851550460',
                'text': text
            }
        )
