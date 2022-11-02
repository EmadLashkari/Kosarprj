from curses import meta
from dataclasses import field
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm


class Profile(UserChangeForm):

    class Meta:
        model = User
        fields = ('username',)
class AddUserForm(UserCreationForm):

    first_name = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1= forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2',)

        
        