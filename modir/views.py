import imp
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LetterForm
from django.contrib.auth.models import AbstractUser
from .models import Letter
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def level(request):
    return render(request , 'modir/level.html')

def adminUsers(request):
    firstname = [f.name for f in User._meta.get_fields()]
    username = User._meta.get_field('username')

    return render(request,'modir/admin-users.html',{'user':username,'first':firstname})

def get_letter(request):
    form = LetterForm
    
    return render(request, 'modir/newletter.html', {'form':form})

def home(request):
    return render(request,'modir/index.html')

def blank(request):
    return render(request,'modir/blank.html')

def LoginView(request):
    return HttpResponseRedirect(reverse('login'))