from django.db import models
import uuid

# Create your models here.

# def file_validator(file):
#     if file.size > 5*1024*1024:
#         raise ValidationError('File size should be less than 5MB')
#     if file.name.split('.')[-1] not in ['pdf']:
#         raise ValidationError('Only pdf files are allowed')



class ArticleForm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    college_name = models.CharField(max_length=100)
    
    title = models.CharField(max_length=100)
    theme = models.CharField(max_length=100)
    word_count = models.CharField(max_length=10)
    
    abstract = models.TextField()
    keywords = models.TextField()
    reference = models.TextField()
    
    confirmation = models.BooleanField(default=False)
    agreement = models.BooleanField(default=False) 
    
    question_1 = models.TextField()
    question_2 = models.TextField()
    
    # article_file = models.FileField(upload_to='articles/', null=False, blank=False, validators=[file_validator])
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
