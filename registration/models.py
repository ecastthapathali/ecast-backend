from django.db import models

# Create your models here.
from django.db import models
import re
import uuid

# Create your models here.

def verify_roll(roll):
    pattern = re.compile(r'^THA\d{3}B[A-Z]{2}\d{3}$')
    return pattern.match(roll)

department_choices = [

    ('BCT', 'Computer Engineering'),
    ('BCE', 'Civil Engineering'),
    ('BEL', 'Electrical Engineering'),
    ('BEI', 'Electronics, Communication and Information Engineering'),
    ('BME', 'Mechanical Engineering'),
    ('BIE', 'Industrial Engineering'),
    ('BAM', 'Automobile Engineering'),
]

batch_choices = [

    ('75', '2075'),
    ('76', '2076'),
    ('77', '2077'),
    ('78', '2078'),
    ('79', '2079'),
    ('80', '2080'),
    ('81', '2081'),
]

class RegistrationForm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    campus_roll = models.CharField(max_length=12, validators=[verify_roll])
    department = models.CharField(max_length=100, choices=department_choices)
    batch = models.CharField(max_length=10, choices=batch_choices)
    filled_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Registration Form'
        verbose_name_plural = 'Registration Forms'
        ordering = ['-filled_date']
        unique_together = ['email']