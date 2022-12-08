from django.contrib import admin
from django.urls import path
from .views import Registerview,Loginview,Userview,Logoutview

urlpatterns = [
    path('register',Registerview.as_view()),
    path('login',Loginview.as_view()),
    path('user',Userview.as_view()),
    path('logout',Logoutview.as_view()),
]