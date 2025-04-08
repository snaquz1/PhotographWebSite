from django.contrib import admin
from django.urls import path
from .views import *

app_name = "MainApp"
urlpatterns = [
    path("", main, name="main"),
    path("examples", examples, name="examples"),
    path("album/<int:album_id>", album, name="album"),
    path("reviews", reviews, name="reviews"),
    path("request", request, name="request"),
    path("requests", requests, name="requests"),
    path("sucess", sucess, name="sucess"),
]