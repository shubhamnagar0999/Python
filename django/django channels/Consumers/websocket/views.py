from django.shortcuts import render
from .models import Group
# Create your views here.
def base(request,group):
    g = Group.objects.filter(name = group).first()
    if g:
        pass
    else:
        groupname = Group(name = group)
        groupname.save()
    return render(request,'base.html',{'group' : group})