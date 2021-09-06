from django.db import models

class FAQs(models.Model):
    #  FaQs
    question = models.CharField(max_length=200)
    answer = models.TextField(blank=True)

def __str__(self):
    return self.question

class Message(models.Model):
    # Messages
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
