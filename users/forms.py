from curses import meta
from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import AddUser

class AddUserForm(ModelForm):
    class Meta:
        model = AddUser
        fields = ['personalCode','name','mobileNumber','phoneNumber','email','address','username','password','group','sign','picture',]

        widgets = {
            'personalCode':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'mobileNumber':forms.TextInput(attrs={'class':'form-control'}),
            'phoneNumber': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'group':forms.Select(attrs={'class':'form-control'}),
            'sign':forms.FileInput(),
            'picture':forms.FileInput()
        }
        