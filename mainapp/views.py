from django.shortcuts import render, HttpResponse
from .task import test_func, send_func
from send_mail_app.task import send_mail_func
from django.core.mail import send_mail
# Create your views here.
def test(request):
    test_func.delay()
    send_func.delay()
    send_mail('toi', 'euler', 'pk6222307@gmail.com', ['paliwalap7@gmail.com'])

    return HttpResponse("Done")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")