from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    title = models.CharField(max_length=100)
    bio = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',null=False, blank=False)
    
    
    def __str__(self):
        return self.title