from django.forms import ModelForm
from .models import *
from django import forms


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields="__all__"
        widgets={
            'full_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}),
            'email': forms.EmailInput(attrs={'class' : 'form-control', 'placeholder': 'Email' }),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Subject'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'})
        }