from django.shortcuts import render, HttpResponse
from .task import test_func, send_func
from send_mail_app.task import send_mail_func
from django.core.mail import send_mail
# Create your views here.

import requests
import json

from send_mail_app.models import RegisteredUser
# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        url = f'https://codeforces.com/api/user.rating?handle={username}'
        response = requests.get(url)
        data = response.text
        parsed = json.loads(data)

        result = parsed['result']
        lastContest = result[-1:]
        details = lastContest[0]

        RegisteredUser(username = username, email=email, oldrating = details['newRating']).save()
        send_mail('CF-rating','You have registered successfully', '', [email])
        return render(request, 'success.html')

    return render(request, 'index.html')

def send_mail_to_all(request):

    # send_mail('Codeforces Ratings Update','Your updated ratings are', '', ['paliwalap7@gmail.com'])
    # return HttpResponse("done")
    return render(request, 'test.html')