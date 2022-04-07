from django.contrib import admin
from Details.models import Detail

# Register your models here.
class Clear(admin.ModelAdmin):
    list_display = ('id','Name','LName','Phone','Email')

admin.site.register(Detail,Clear)