from django.db import models
from home.models import User
from event.models import Event
# Create your models here.

class Attend(models.Model):
    attend_id = models.AutoField(auto_created=True, primary_key=True)
    title = models.ForeignKey(Event, on_delete=models.CASCADE)
    email = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'attend' 