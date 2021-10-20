from django.db import models

# Create your models here.
class RegisteredUser(models.Model):
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=45)
    oldrating = models.IntegerField()

    def __str__(self):
        return self.username
