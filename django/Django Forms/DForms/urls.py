from django.urls import path
from DForms import views


urlpatterns = [
    path('',views.base),
    path('Show/',views.show,name='show')
]
