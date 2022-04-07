
from telnetlib import DET
from django.contrib import admin
from .models import Detail
# Register your models here.
# @admin.register(Detail)
# class Admin(admin.ModelAdmin):
#     list_display = ('Name','Last')


admin.site.register(Detail)
