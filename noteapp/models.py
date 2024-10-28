from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
    
User = get_user_model()
# Create your models here.


    
class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=5000000000)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Alarm(models.Model):
    caption = models.CharField(max_length=50, null=True)
    songs = models.FileField(upload_to='alarm', null=True, blank=True)
    
    def __str__(self):
        return self.caption