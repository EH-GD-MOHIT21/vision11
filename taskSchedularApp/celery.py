from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vision11.settings')
app = Celery('taskSchedularApp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'print_msg_main': {
        'task': 'print_msg_main',       
        'schedule': 80.0,
        'options': {
            'expires': 15.0,
        },
        # 'args': ("Hello",) 
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
