from django.core.mail import send_mail as _send_mail
from django.conf import settings


def send_mail(to, subject, message):
    """
        Return True if mail successfully delivered
        otherwise returns False.
        Syntax:
            send_mail(to=['abc@def.com',],subject="Hello World!",message="Welcome to programming.")
    """
    try:
        _send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            to,
            fail_silently=False,
        )
        return True
    except Exception as e:
        return False
