from django.db import models

# Create your models here.
class Message(models.Model):
    #time_created = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length = 20)
    recipient = models.CharField(max_length= 20)
    messagebody = models.CharField(max_length=1000)
