import imp
from tokenize import Name
from django import forms

class UserInput(forms.Form):
    Name = forms.CharField()
    Phone = forms.IntegerField()