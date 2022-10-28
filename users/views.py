from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import AddUserForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import AddUser
from django.urls import reverse
# Create your views here hoow.

 class UserCreat(CreateView):
#     model = AddUser
#     fields = ['personalCode','name','mobileNumber','phoneNumber','email',
#     'address','username','password','group','sign','picture']

def user_add(request):
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddUserForm(request.POST)
        
        if form.is_valid():
            form.save()

            obj = AddUser.objects.first()
            User.objects.create_user(getattr(obj, 'username'),getattr(obj, 'email')
            , getattr(obj, 'password'))

            return HttpResponseRedirect(reverse('modir:adminUsers'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddUserForm()

   
    return render(request, 'users/add_user.html',{'form':form})