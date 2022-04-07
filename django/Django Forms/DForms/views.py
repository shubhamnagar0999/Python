import imp
from unicodedata import name
from django.http import request
from django.shortcuts import render
from .Forms import UserInput
from .models import User
# Create your views here.
def base(request):
    ui = UserInput()
    return render(request,'Base.html',{'form':ui})

def show(request):
    if request.method=='POST':
        db = User.objects.all()
        ui = UserInput(request.POST)
        if ui.is_valid():
            name = ui.cleaned_data['Name']
            phone = ui.cleaned_data['Phone']
            db = User(Name=name,Phone=phone)
            db.save()
        else:
            ui = UserInput()
    return render(request,'Show.html',{'data':ui})