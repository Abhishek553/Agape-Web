from django.urls import path
from home import views
urlpatterns = [
    path('index', views.index),
    path('login', views.login),
    path('register', views.register),
]
