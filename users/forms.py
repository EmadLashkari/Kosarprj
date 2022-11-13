from curses import meta
from dataclasses import field
from django import forms
from django.forms import ModelForm
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
# from .models import UserProfile

# class Profile(UserChangeForm):
    
#     personalcode = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
#     user = forms.Select(attrs={'class':'form-control'})
    

#     class Meta:
#         model = UserProfile
#         fields = ('user','personalcode')

class AddUserForm(UserCreationForm):
    personalcode = forms.CharField(max_length = 20,widget=forms.TextInput(attrs={'class':'form-control'}))
    mobileNumber = forms.CharField(max_length = 20,widget=forms.TextInput(attrs={'class':'form-control'}))
    phoneNumber = forms.CharField(max_length = 20,widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1= forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))
    groups = forms.Select(attrs={'class':'form-control'})
    
    class Meta:
        model = CustomUser
        fields = ('personalcode','mobileNumber','phoneNumber','address','first_name','last_name', 'username', 'email', 'password1' ,'password2','groups')

        
        