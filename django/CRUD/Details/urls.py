import imp
from Details import views
from django.urls import path
from django.contrib import admin

urlpatterns = [

    path('', views.base,name='Home'),
    path('admin/', admin.site.urls),
    path('Contect/',views.contect,name='Contect'),
    path('Table/',views.table,name='table'),
    path('Delete/<int:id>',views.delete,name='delete'),
    path('Update/<int:id>',views.update,name='update'),
    path('Update/',views.table,name='update'),

]
