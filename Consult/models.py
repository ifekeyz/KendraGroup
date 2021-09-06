from django.db import models

class Consulting(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    