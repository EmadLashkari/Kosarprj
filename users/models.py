from operator import mod
from django.contrib.auth.models import User
from django.db import models

from modir.views import blank

# add user models and form
class AddUser(models.Model):
    groupsName = [('admin','مدیر'),('dabir','دبیر'),('user','کاربر')]
    personalCode = models.IntegerField()
    name = models.CharField(max_length = 50)
    mobileNumber = models.IntegerField()
    phoneNumber = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    group = models.CharField(max_length = 50,choices=groupsName)
    sign = models.FileField(blank=True,null=True)
    picture = models.FileField(blank=True,null=True)

    
    

