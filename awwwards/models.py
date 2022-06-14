from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    bio = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    picture = models.ImageField(null=True, blank=True,upload_to='images')


    def __str__(self):
        return f'{self.author.username} Profile'
    
class Site(models.Model):
    name = models.TextField()
    url= models.URLField()
    image = models.ImageField(null=False,blank=False)
    date_posted = models.DateTimeField(default=timezone.now)