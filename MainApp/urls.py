from django.contrib import admin
from django.urls import path
from .views import *

app_name = "MainApp"
urlpatterns = [
    path("", main, name="main"),
    path("examples", examples),
    path("album/<int:album_id>", album),
]