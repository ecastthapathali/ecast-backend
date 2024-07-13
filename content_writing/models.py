from django.db import models

class ContentForm(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    email = models.EmailField(unique=True,max_length=200)
    phone = models.IntegerField(unique=True)
    
