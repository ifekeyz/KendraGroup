from django.db import models
from datetime import datetime

class Team(models.Model):
    
    # Team
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    position = models.CharField(max_length=200)
    hire_date = models.DateField(auto_now_add=False)
    facebook = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    whatsApp = models.CharField(max_length=100)
    is_mvp = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Slider(models.Model):

    #Slider and About image
    SliderName = models.CharField(max_length=200)
    slider1 =  models.ImageField(upload_to='photos/%Y/%m/%d/')
    slider2 =  models.ImageField(upload_to='photos/%Y/%m/%d/')
    slider3 =  models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.SliderName
    
