from django import forms
from django.forms.fields import EmailField
from django.forms.forms import Form

#create your forms here

class FormClass(forms.Form):
    Name=forms.CharField(max_length=100)
    Age=forms.IntegerField()
    Email=forms.EmailField()
    Place=forms.CharField(max_length=100)
    Password=forms.CharField(max_length=100)
    Re_Enter_Password=forms.CharField(max_length=100)

    