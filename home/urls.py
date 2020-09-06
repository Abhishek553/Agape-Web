from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="main"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="register"),
    path('starting/', views.starting, name="start"),
]
