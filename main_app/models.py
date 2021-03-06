from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Location(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200, default = 'city')
    state = models.CharField(max_length=200, default = 'state')
    img = models.CharField(max_length=700)
    lat = models.FloatField(max_length=100, default= 37.8393)
    lng = models.FloatField(max_length=100, default=86.27)
    description = models.TextField(max_length=700)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['state']
    

class Comment(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date_posted = models.DateTimeField(default = timezone.now)
    comment = models.TextField(max_length=700)

    def __str__(self):
        return self.comment


