from django.db import models

#create your model here
class User(models.Model):

    name = models.CharField(max_length=100)
    collage_org = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "users"

