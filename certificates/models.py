import secrets
import string
from django.db import models

def generate_random_uid():
    characters = string.ascii_letters + string.digits  
    uid = ''.join(secrets.choice(characters) for _ in range(36))  
    
    
    formatted_uid = '-'.join([uid[i:i+4] for i in range(0, len(uid), 4)])
    return formatted_uid

class ParticipationCertificate(models.Model):
    name = models.CharField(max_length=100)  
    event_name = models.CharField(max_length=200)  
    date = models.DateField()  
    custom_id = models.CharField(max_length=44, unique=True, default=generate_random_uid)  
    generated_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f'{self.name} - {self.event_name}'
