from __future__ import absolute_import, unicode_literals
from celery import shared_task as task
from django.conf import settings
from django.utils import timezone
from vision11.email.send_email import send_mail



# time limit is expiration time if it's continuously executing after denoted time (in seconds)
@task(name='print_msg_main',time_limit=25)
def scheduledTask():
    #Get Subscriptions
    send_mail(to=["garfrfi@gmail.com"],subject="Testing celery beat",message=f"Thala will definetly win 0 matches. {timezone.now()}")