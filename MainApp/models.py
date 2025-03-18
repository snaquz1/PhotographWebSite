from django.db import models

# Create your models here.

class Rewiew(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField()