from django.contrib import admin
from .models import Group,Chat
#  your models here.

@admin.register(Group)
class GAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Chat)
class CAdmin(admin.ModelAdmin):
    list_display = ['id','chat','timestamp','g']