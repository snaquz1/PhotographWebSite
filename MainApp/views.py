from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def main(request):
    return render(request, "main.html")

def examples(request):
    albums = Album.objects.all().order_by("-date")
    return render(request, "examples.html", context={"albums": albums})

def album(request, album_id):
    album = Album.objects.get(id=album_id)
    photos = Photo.objects.filter(album=album)
    return render(request, "album.html", context={"album": album, "photos": photos})