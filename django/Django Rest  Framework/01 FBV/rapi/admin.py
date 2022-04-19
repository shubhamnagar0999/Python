from django.contrib import admin
from rapi.models import signup

# Register your models here.
class modal(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(signup,modal)