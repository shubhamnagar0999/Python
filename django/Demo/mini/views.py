from django.shortcuts import render

from .models import Detail

# Create your views here.
def index(request):
    d = Detail.objects.all()
    return render(request,'Base.html',{'d':d})

def first(request):
    return render(request,'First.html')