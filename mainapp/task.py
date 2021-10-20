from celery import shared_task
from django.core.mail import send_mail

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done"

@shared_task(bind=True)
def send_func(self):
    send_mail('toi', 'euler', 'pk6222307@gmail.com', ['paliwalap7@gmail.com'])
