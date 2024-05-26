from django.db import models

# Create your models here.

class Intake(models.Model):
        # list for positions available for intake
    POSITION = [                          
        ('Editor', 'Editor'),                      
        ('Communication_and_HR', 'Communication and HR'),
        ('Technical_Team', 'Technical Team'),
        ('Event_Manager', ' Event Manager'),
        ('Social_Media_Manager', 'Social Media Manager'),
        ('Research_Team', 'Research_Team'),
        ('General_Member', 'General Member'),
    ]

    # list of faculties 
    FACULTY = [
        ('BCT', 'BCT'),
        ('BEI', 'BEI'),
    ]

    # list of batches of intake
    BATCH = [
        ('2077', '2077'),
        ('2078', '2078'),
        ('2079', '2079'),
        ('2080', '2080'),
    ]

    roll = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=5, choices=FACULTY, null=True)     
    batch = models.CharField(max_length=5, choices=BATCH, null=True)
    email = models.EmailField(null=True)
    contact = models.CharField(max_length=14, null=True)
    introduction = models.TextField(null=True)
    position= models.CharField(max_length=25, choices=POSITION, null=True)
    cv = models.FileField(upload_to='intake_cv/', blank=True)                   
    opinion = models.TextField(null=True, blank=True)                       
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)



def __str__(self):
    return self.roll
