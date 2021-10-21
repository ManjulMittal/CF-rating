# CF-ratings
This is a backend project that fetches the data from your codeforces profile with the help of the codeforces API and uses it to generate a mail at your gmail id whenever the ratings are updated on the codeforces profile.
This will check for the ratings changes every single minute and sends you an update as soon as the ratings take an effect so that you dont have to check the ratings everytime.
This supports multiple users with the help of integrated database and updated all the registered users in the profile and does not send a mail if it does not see changes.
built with django framework with the help of redis and celery which are responsible for the mail creation and checking of the ratings every minute.
