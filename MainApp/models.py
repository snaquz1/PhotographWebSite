import datetime

from django.db import models

# Create your models here.

class Rewiew(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField()

class Album(models.Model):
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='albumcovers')
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='albumphotos')

    def __str__(self):
        return self.album.title
