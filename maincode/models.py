from django.db import models

# Create your models here.

class tododata(models.Model):
    title = models.CharField(max_length = 255)
    description = models.CharField(max_length =255)
    completed = models.BooleanField(default=False)

def __str__(self):
    return self.title

