import imp
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LetterForm
from django.contrib.auth.models import AbstractUser
from .models import Letter
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


def adminUsers(request):
    #perm  = ModelBackend.has_perm()
    #userobj = AddUser.objects.all()
    return render(request,'modir/admin-users.html')

def get_letter(request):
    form = LetterForm
    
    return render(request, 'modir/newletter.html', {'form':form})

def home(request):
    return render(request,'modir/index.html')

def blank(request):
    return render(request,'modir/blank.html')

def LoginView(request):
    return HttpResponseRedirect(reverse('login'))