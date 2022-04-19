
from django.urls import path
from .views import CBVStudents, CBVTeacher
# from aboutns import views
urlpatterns = [
    path('students/',CBVStudents.as_view()),
    path('teachers/',CBVTeacher.as_view()),
   
]
