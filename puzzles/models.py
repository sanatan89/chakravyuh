from django.db import models

# Create your models here.

class Questions(models.Model):
    description = models.TextField(blank=True)
    level = models.IntegerField(null=True)
    image = models.ImageField(upload_to='question_image', blank=True)
    answer = models.CharField(max_length=100,blank=True)
    
