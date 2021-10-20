from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_with_django.settings')

app = Celery('celery_with_django')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace = 'CELERY')

app.autodiscover_tasks()
# Celery beat settings
app.conf.beat_schedule = {
    'send_mail-every-30sec':{
        'task':'send_mail_app.task.send_mail_func',
        'schedule':crontab(minute='*/1'),
        
    }
}



@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request}')