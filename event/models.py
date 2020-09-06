from django.db import models

# Create your models here.
class Event(models.Model):

    title = models.CharField(max_length=50)
    date = models.CharField(max_length=10)
    text = models.CharField(max_length=500)
    image = models.FileField(upload_to='static/images/upload')

    class Meta:
       db_table = "event"

