from django.db import models
from datetime import datetime
from Pages.models import Team

class Houserent(models.Model):
    # Houserent
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    brief = models.CharField(max_length=100)
    price = models.IntegerField()
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    landsize = models.CharField(max_length=100)
    garage = models.IntegerField()
    squareFeet = models.CharField(max_length=100)
    listingDate = models.DateField(auto_now_add=False)
    # listingDate = models.DateTimeField(default = datetime.now, blank=True)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.location