from django.db import models

class IntakeForm(models.Model):
    
    # list for positions available for intake
    POSITION = [                                                
        ('Communication_and_HR', 'Communication and HR'),
        ('Software_Cordinator', 'Software Cordiantor'),
        ('Graphic_Designer', 'Graphic Designer'),
        ('Hardware_Cordinator', 'Hardware Cordiantor'),
        ('Event_Manager', ' Event Manager'),
        ('Social_Media_Manager', 'Social Media Manager'),
        ('Research', 'Research'),
        ('General_Member', 'General Member'),
    ]

    # list of faculties 
    FACULTY = [
        ('BCT', 'BCT'),
        ('BEI', 'BEI'),
    ]

    # list of batches of intake
    BATCH = [
        ('2076', '2076'),
        ('2077', '2077'),
        ('2078', '2078'),
        ('2079', '2079'),
        ('2080', '2080'),
    ]


    intake_name = models.CharField(max_length=50)                                  
    intake_rollno = models.CharField(max_length=12)
    intake_faculty = models.CharField(max_length=5, choices=FACULTY, null=True)     
    intake_batch = models.CharField(max_length=5, choices=BATCH, null=True)
    intake_email = models.EmailField(unique=True)
    intake_phn = models.CharField(max_length=15)                                    # for contact number of the intake
    intake_introduction = models.TextField(null=True)
    intake_position= models.CharField(max_length=25, choices=POSITION)
    intake_cv = models.FileField(upload_to='intake_cv/', blank=True)
    intake_experience = models.TextField(null=True, blank=True)                     # for the experience of intake in different technology
    intake_opinion = models.TextField(null=True, blank=True)                        # for the opinion or idea of intake 
    intake_facebook = models.URLField(blank=True)
    intake_linkedin = models.URLField(blank=True)
    intake_github = models.URLField(blank=True)
