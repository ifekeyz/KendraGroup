from django.db import models

# Create your models here.
class Landsale(models.Model):
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    image2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    image3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    details = models.CharField(max_length=100)
    price = models.IntegerField()
    landsize = models.CharField(max_length=100)
    description = models.TextField()
    listingDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.location
    