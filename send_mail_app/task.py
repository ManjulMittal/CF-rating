from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail

from send_mail_app.models import RegisteredUser

@shared_task(bind=True)
def send_mail_func(self):
    users = RegisteredUser.objects.all()
    
    for user in users:
        import json
        import requests
        url = f'https://codeforces.com/api/user.rating?handle={user.username}'
        
        response = requests.get(url)
        data = response.text
        parsed = json.loads(data)

        result = parsed['result']
        lastContest = result[-1:]
        details = lastContest[0]

        if(details['newRating'] != user.oldrating):
            user.oldrating = details['newRating']
            user.save()
            send_mail('toi', str(details['newRating']), 'pk6222307@gmail.com', [user.email])
    
    return 'Done'


# import json
# import requests
# url = 'https://codeforces.com/api/user.rating?handle=maddler'
 
# response = requests.get(url)
# data = response.text
# parsed = json.loads(data)

# result = parsed['result']
# lastContest = result[-1:]
# details = lastContest[0]
# print(details['ratingUpdateTimeSeconds'])
# print(details['oldRating'])
# print(details['newRating'])