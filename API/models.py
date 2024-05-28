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
    email = models.EmailField(null=False)
    contact = models.CharField(max_length=14, null=False)
    describe_yourself = models.TextField(null = False)
    position= models.CharField(max_length=25, choices=POSITION, null=False)
    cv = models.FileField(upload_to='intake_cv/', blank=True)                   
    hope_to_gain = models.TextField(null=False) 
    interest = models.TextField(null=True, blank=True) 
    other = models.TextField(null=True, blank=True) 
    social_media = models.URLField(blank=True)


def __str__(self):
    return self.roll
