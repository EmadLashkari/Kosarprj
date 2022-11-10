from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Letter , Level


class NewLevelFrom(ModelForm):
    class Meta:
        model = Level
        fields = ['name','nameplz','sign','parentID']
        labels = {
            'name':'نام'
            ,'nameplz':'نام محترمانه'
            ,'sign':'حق امضا',
            'parentID':'شماره جدول'

        }

class LetterForm(ModelForm):
    class Meta:
        model = Letter
        fields = ['position','signatory','secretariat'
        ,'receivers','Transcript','subtitle','discription','ready_text','size_letter']
        labels = {
            'position':'ارسال کننده:'
            ,'signatory':'امضا کننده:',
            'secretariat':'انتخاب دبیرخانه:',
            'receivers':'گیرندگان:',
            'Transcript':'رونوشت:',
            'subtitle':'عنوان نامه:',
            'discription':'توضیحات:',
            'ready_text':'',
            'size_letter':'سایز برگه:',
            
        }

        # widgets = {
        #     'signatory':forms.Select(attrs={'class':'w3-input'}),
        #     'secretariat':forms.Select(attrs={'class':'w3-input'}),
        #     'position': forms.Select(attrs={'class':'w3-input'}),
        #     'Transcript':forms.CheckboxSelectMultiple(attrs={'class':'w3-input'}),
        #     'receivers': forms.CheckboxSelectMultiple(attrs={'class':'w3-input'}),
        #     'subtitle':forms.TextInput(attrs={'class':'form-control'}),
        #     'discription':forms.Textarea(attrs={'class':'form-control'}),
        #     'ready_text':forms.Select(attrs={'class':'w3-input'}),
        #     'size_letter':forms.RadioSelect(attrs={'class':'radio'}),
        # }
       