from django.urls import path
from home import views
urlpatterns = [
    path('index/', views.index),
    path('login', views.loginPage),
    path('register', views.register),
    path('starting', views.starting)
]
