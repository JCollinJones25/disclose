from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200, default = 'city')
    state = models.CharField(max_length=200, default = 'state')
    img = models.CharField(max_length=700)
    description = models.TextField(max_length=700)
    lat = models.FloatField(max_length=100, default= 37.8393)
    lng = models.FloatField(max_length=100, default=86.27)
    img2 = models.CharField(max_length=700, default="https://us.123rf.com/450wm/pavelstasevich/pavelstasevich1811/pavelstasevich181101028/112815904-no-image-available-icon-flat-vector-illustration.jpg?ver=6" )
    img3 = models.CharField(max_length=700, default="https://us.123rf.com/450wm/pavelstasevich/pavelstasevich1811/pavelstasevich181101028/112815904-no-image-available-icon-flat-vector-illustration.jpg?ver=6")
    img4 = models.CharField(max_length=700, default="https://us.123rf.com/450wm/pavelstasevich/pavelstasevich1811/pavelstasevich181101028/112815904-no-image-available-icon-flat-vector-illustration.jpg?ver=6")
    


    def __str__(self):
        return self.name