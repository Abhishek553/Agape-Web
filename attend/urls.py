from django.urls import path
from attend import views
urlpatterns = [
    path('', views.index, name="attend"),
    path('attend', views.attend),
    
]
