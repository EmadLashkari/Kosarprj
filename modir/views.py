import imp
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LetterForm, NewLevelFrom
from django.contrib.auth.models import AbstractUser
from .models import Letter
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from users.models import UserProfile


class new_level(CreateView):
    form_class = NewLevelFrom
    template_name = 'modir/new_level.html'
    success_url = reverse_lazy('modir:adminUsers')

    def get_object(self):
        return self.request.user

def level(request):
    return render(request , 'modir/level.html')

def adminUsers(request):
    userfields = User.objects.all()
    profile = UserProfile.objects.all()
    
    return render(request,'modir/admin-users.html',{'field':userfields,'profile':profile})

class get_letter(CreateView):
    form_class = LetterForm
    template_name = 'modir/newletter.html'
    success_url = reverse_lazy('modir:home')

    def get_object(self):
        return self.request.user

def home(request):
    return render(request,'modir/index.html')

def blank(request):
    return render(request,'modir/blank.html')

def LoginView(request):
    return HttpResponseRedirect(reverse('login'))