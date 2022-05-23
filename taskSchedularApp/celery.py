from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vision11.settings')
app = Celery('taskSchedularApp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'get_live_score': {
        'task': 'get_live_score',       
        'schedule': 180.0,  # every 10 minutes (10*60 seconds)
        'options': {
            'expires': 15.0,
        },
        # 'args': ("Hello",)
    },

    'fetch_match_list':{
        'task': 'fetch_match_list',       
        'schedule': crontab(hour=0, minute=10),  # every day at 0:10 AM hours GMT
        'options': {
            'expires': 15.0,
        },
    }, 

    # Executes every Monday morning at 1:30 a.m. GMT
    'updateteamorplayers': {
        'task': 'updateteamorplayers',
        'schedule': crontab(hour=1, minute=30, day_of_week=1),
    },
}