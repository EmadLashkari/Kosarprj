from curses import meta
from dataclasses import field
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AddUserForm(UserCreationForm):

    #groupsName = [('admin','مدیر'),('dabir','دبیر'),('user','کاربر')]
    #personalCode = forms.IntegerField()
    first_name = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class':'form-control'}))
    #mobileNumber = forms.IntegerField()
    #phoneNumber = forms.IntegerField()
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    #address = forms.CharField(max_length = 50)
    username = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1= forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))
    #group = forms.ChoiceField(choices=groupsName)
    # sign = forms.FileField(allow_empty_file=True)
    # picture = forms.FileField(allow_empty_file=True)
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2',)

        # widgets = {
        #     'personalCode':forms.TextInput(attrs={'class':'form-control'}),
        #     'first_name':forms.TextInput(attrs={'class':'form-control'}),
        #     'last_name':forms.TextInput(attrs={'class':'form-control'}),
        #     'mobileNumber':forms.TextInput(attrs={'class':'form-control'}),
        #     'phoneNumber': forms.TextInput(attrs={'class':'form-control'}),
        #     'email':forms.TextInput(attrs={'class':'form-control'}),
        #     'address':forms.TextInput(attrs={'class':'form-control'}),
        #     'username':forms.TextInput(attrs={'class':'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'class':'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class':'form-control'}),
        #     'group':forms.Select(attrs={'class':'form-control'}),
        #     # 'sign':forms.FileInput(),
        #     # 'picture':forms.FileInput()
        # }
        