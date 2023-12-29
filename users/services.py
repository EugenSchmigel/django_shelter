from django.conf import settings
from django.core.mail import send_mail


def send_new_password(email, new_password):
    send_mail(
        subject='You have changed the password.',
        message=f'Your new password: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
