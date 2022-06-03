from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)
    img = models.CharField(max_length=700)
    description = models.TextField(max_length=700)