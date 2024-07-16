from django.db import models

class ContentForm(models.Model):
    department_choices = [

    ('BCT', 'Computer Engineering'),
    ('BCE', 'Civil Engineering'),
    ('BEL', 'Electrical Engineering'),
    ('BEI', 'Electronics, Communication and Information Engineering'),
    ('BME', 'Mechanical Engineering'),
    ('BIE', 'Industrial Engineering'),
    ('BAM', 'Automobile Engineering'),
]
    
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    email = models.EmailField(unique=True,max_length=200)
    phone = models.IntegerField(unique=True)
    department = models.CharField(choices=department_choices,max_length=100,null=True)
    file = models.FileField(upload_to="articles/",null=True)
    
