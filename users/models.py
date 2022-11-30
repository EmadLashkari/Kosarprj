from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    personalcode = models.CharField(max_length=20, null=True, help_text='حداکثر ۲۰ کارکتر فقط اعداد ۰تا۹')
    mobileNumber = models.CharField(max_length=20, null=True)
    phoneNumber = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)

    
# add user models and form
# class UserProfile(models.Model):
#     user = models.OneToOneField(User , on_delete=models.CASCADE , default= User.username )
#     personalcode = models.IntegerField()
#     phone_number = models.CharField(max_length=20 ,null=True)


    # def __str__(self):
    #     return self.user.user_name
    
