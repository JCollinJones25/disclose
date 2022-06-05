from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200, default = 'city')
    state = models.CharField(max_length=200, default = 'state')
    img = models.CharField(max_length=700)
    description = models.TextField(max_length=700)