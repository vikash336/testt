from django.urls import URLPattern,path

from testapp import views

from .views import CR , UD

urlpatterns=[
    path('general/', CR.as_view()),
    path('general/<id>', UD.as_view()),
    
]