from django.db import models
import uuid
from django.core.exceptions import ValidationError

# Create your models here.

theme_choices = [
    ('Emerging Technologies','Emerging Technologies'),
    ('Artificial Intelligence and Machine Learning', 'Artificial Intelligence and Machine Learning'),
    ('Cybersecurity and Privacy', 'Cybersecurity and Privacy'),
    ('Innovation and Future Trends', 'Innovation and Future Trends'),
    ('Technology in Society', 'Technology in Society')
]

def file_validator(file):
    # if file.size > 5*1024*1024:
    #     raise ValidationError('File size should be less than 5MB')
    if file.name.split('.')[-1] not in ['pdf', 'doc', 'docx']:
        raise ValidationError('Only docs or pdf files are allowed')

def word_count_validator(value):
    if value < 800 or value > 1200:
        raise ValidationError('NUmber of words is Invalid!')


class ArticleForm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    college_name = models.CharField(max_length=100)
    
    title = models.CharField(max_length=100)
    theme = models.CharField(max_length=100, choices=theme_choices)
    word_count = models.IntegerField(validators=[word_count_validator])
    
    abstract = models.TextField()
    keywords = models.TextField()
    reference = models.TextField()
    
    confirmation = models.BooleanField(default=False)
    agreement = models.BooleanField(default=False) 
    
    question_1 = models.TextField()
    question_2 = models.TextField()
    
    article_file = models.FileField(upload_to='articles/', null=False, blank=False, validators=[file_validator])
    
    # facebook_link = models.URLField(blank=True, null=True)
    # suggestion = models.TextField()
    
    filled_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Article Form'
        verbose_name_plural = 'Article Forms'
        ordering = ['-filled_date']
        unique_together = ['email']
