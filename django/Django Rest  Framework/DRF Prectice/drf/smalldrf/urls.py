from django.urls import path
from smalldrf import views
from .views import stud,studpk,M_and_G,M_and_G_pk,Generic,Generic_pk

urlpatterns = [
    # url for function based view
    path("",views.home),
    path("<int:id>",views.d_u),
    
    # url for class based view
    path("classview/",stud.as_view()),
    path("classview/<int:id>",studpk.as_view()),

    #url for mixins and generics
    path("m_and_g/",M_and_G.as_view()),
    path("m_and_g/<int:pk>",M_and_G_pk.as_view()),

    #url for generics
    path("generics/",Generic().as_view()),
    path("generics/<int:pk>",Generic_pk.as_view()),
]
