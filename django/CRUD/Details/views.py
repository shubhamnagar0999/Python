from http.client import HTTPResponse
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from .models import Detail

# Create your views here.
def base(request):
    return render(request,'Home.html') 

def contect(request):
    if request.method=='POST':
        Name = request.POST.get('name')
        LName = request.POST.get('lname')
        Phone = request.POST.get('phone')
        Email = request.POST.get('email')
        save = Detail(Name=Name,LName=LName,Phone=Phone,Email=Email)
        save.save()
    return render(request,'Contect.html')

def table(request):
    data = Detail.objects.all()
    return render(request,'Table.html',{'data' : data})

def delete(request,id):
    if request.method=='GET':
        rm = Detail.objects.get(id=id)
        rm.delete()

    
    data = Detail.objects.all()
    return render(request,'Table.html',{'data':data})

def update(request,id):
    update = Detail.objects.get(id=id)
    print(update)
    if request.method=='POST':
        Name = request.POST.get('name')
        LName = request.POST.get('lname')
        Phone = request.POST.get('phone')
        Email = request.POST.get('email')
        update.Name = Name
        update.LName = LName
        update.Phone = Phone
        update.Email = Email
        update.save()
    return render(request,'Update.html',{'udata':update})