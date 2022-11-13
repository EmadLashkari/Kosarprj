from django.http import HttpResponseRedirect
from django.shortcuts import render
from users.models import CustomUser
from .forms import AddUserForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
# from .models import UserProfile
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm , UserChangeForm

# Create your views here hoow.

class Profile(generic.UpdateView):
    model = CustomUser
    fields = ['personalcode','mobileNumber','phoneNumber','address','first_name','last_name', 'username', 'email','groups']
    template_name = 'users/profile.html'
    success_url = reverse_lazy('modir:adminUsers')

    def get_object(self):
        return self.request.user


class AddUser(generic.CreateView):
    form_class = AddUserForm
    template_name = 'users/add_user.html'
    success_url = reverse_lazy('modir:adminUsers')

    def get_object(self):
        return self.request.user

# def user_add(request):
    
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = AddUserForm(request.POST)
        
#         if form.is_valid():
#             form.save()

#             return HttpResponseRedirect(reverse('modir:adminUsers'))

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = AddUserForm()

   
#     return render(request, 'users/add_user.html',{'form':form})