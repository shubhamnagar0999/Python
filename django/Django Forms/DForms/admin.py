import imp
from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class useradmin(admin.ModelAdmin):
    list_display = ('Name','Phone')