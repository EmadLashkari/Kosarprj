from operator import mod
from django.contrib.auth.models import User
from django.db import models



# add user models and form
class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    personalcode = models.IntegerField()

    def __str__(self):
        return self.user
    
