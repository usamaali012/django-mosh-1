from django.urls import path
from . import views


# URL Configuration model 
urlpatterns = [
    path('hello/', views.sayHello)
]