import imp
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LetterForm, NewLevelFrom , PostAppoinmentForm , RootForm , DabirKhoneForm
from django.contrib.auth.models import AbstractUser
from .models import Letter , DabirKhone, PostAppoinment , Level
from django.contrib.auth.backends import ModelBackend
from users.models import CustomUser
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
# from users.models import UserProfile

class AddDabirkhone(CreateView):
    form_class = DabirKhoneForm
    template_name = 'modir/add_dabirkhone.html'
    success_url = reverse_lazy('modir:dabirkhone')

    def get_object(self):
        return self.request.user


class Root(CreateView):
    form_class = RootForm
    template_name = 'modir/add_Root.html'
    success_url = reverse_lazy('modir:adminUsers')

    def get_object(self):
        return self.request.user


class postAppoinment(CreateView):
    form_class = PostAppoinmentForm
    template_name = 'modir/PostAp.html'
    success_url = reverse_lazy('modir:adminUsers')

    def get_object(self):
        return self.request.user

class new_level(CreateView):
    form_class = NewLevelFrom
    template_name = 'modir/new_level.html'
    success_url = reverse_lazy('modir:adminUsers')

    def get_object(self):
        return self.request.user

def level(request):
    level = Level.objects.all()
    return render(request , 'modir/level.html', {'Level':level})

def adminUsers(request):
    userfields = CustomUser.objects.all()
    # profile = UserProfile.objects.all()
    
    return render(request,'modir/admin-users.html',{'field':userfields})

class get_letter(CreateView):
    form_class = LetterForm
    template_name = 'modir/newletter.html'
    success_url = reverse_lazy('modir:home')

    def get_object(self):
        return self.request.user

    

def home(request):
    letter = Letter.objects.all()

    return render(request,'modir/index.html', {'letter':letter})

def blank(request):
    return render(request,'modir/blank.html')

def LoginView(request):
    return HttpResponseRedirect(reverse('login'))

def dabirkhone(request):
    dabir = DabirKhone.objects.all()
    post = PostAppoinment.objects.all()
    return render(request,'modir/dabirkhone.html', {'dabir': dabir, 'Post':post })