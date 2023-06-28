from django.db import models

# Create your models here.

class IntakeForm(models.Model):
    POSITION = [
        ('Software Cordinator', 'Software_Cordiantor'),
        ('Graphic Designer', 'Graphic_Dedigner'),
        ('Hardware Cordinator', 'Hardware_Cordiantor'),
    ]
    intake_name = models.CharField(max_length=50)
    intake_rollno = models.CharField(max_length=12)
    intake_email = models.EmailField()
    intake_position= models.CharField(max_length=25, choices=POSITION)
    intake_cv = models.FileField(upload_to='intake_cv/')