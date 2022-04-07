from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def registration(request):
    D = UserCreationForm()
    return render(request,'Registration.html',{'F':D})

def saveRegistration(request):
    D = UserCreationForm()
    if request.method == 'POST':
        D = UserCreationForm(request.POST)
        if D.is_valid():
            D.save()
    return render(request,'Registration.html',{'F':D})

# def registration(request):
#     D = User()
#     return render(request,'Registration.html',{'F':D})

    