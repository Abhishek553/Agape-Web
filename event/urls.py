from django.urls import path
from event import views
urlpatterns = [  
    path('event/', views.event, name="event"),
    path('delete/<int:id>',views.delete),
]
