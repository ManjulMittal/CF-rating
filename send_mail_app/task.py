from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail


@shared_task(bind=True)
def send_mail_func(self):
    send_mail('toi', 'euler', 'pk6222307@gmail.com', ['paliwalap7@gmail.com'])
    return 'Done'
