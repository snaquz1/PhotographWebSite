from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *
from .forms import *

def contains_digit(s):
    return any(char.isdigit() for char in s)


#############################################
def main(request):
    return render(request, "main.html")

def examples(request):
    albums = Album.objects.all().order_by("-date")
    return render(request, "examples.html", context={"albums": albums})

def album(request, album_id):
    album = Album.objects.get(id=album_id)
    photos = Photo.objects.filter(album=album)
    return render(request, "album.html", context={"album": album, "photos": photos})

def reviews(request):
    if request.method == "GET":
        form = ReviewForm()
        review_submitted = request.session.get("review_submitted")
        reviews = Rewiew.objects.all().order_by("-date")
        return render(request, "reviews.html", context={"reviews": reviews, "form": form, "review_submitted": review_submitted})
    elif request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            rate = form.cleaned_data["rate"]
            text = form.cleaned_data["text"]
            Rewiew.objects.create(name=name, rate=rate, text=text).save()
            request.session["review_submitted"] = True
            return redirect("MainApp:reviews")


def sucess(request):
    if request.session.get("request_submitted"):
        del request.session["request_submitted"]
        return render(request, "sucess.html")
    return HttpResponseNotFound("Не найдено")

def request(request):
    form = RequestForm()
    request_submitted = request.session.get("request_submitted")
    if request.method == "GET":
        return render(request, "request.html", context={"form": form, "request_submitted": request_submitted})
    elif request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            if Request.objects.filter(name=name, phone=phone).exists():
                return HttpResponse("Такая заявка уже существует <a href='request'>Вернуться</a>")
            elif len(phone) > 11 or len(phone) < 11 or not phone.isdigit():
                return HttpResponse("Номер телефона должен состоять из 11 цифр <a href='request'>Вернуться</a>")
            elif name.isdigit() or contains_digit(name) or not name.isalpha():
                return HttpResponse("Имя не должно состоять из цифр <a href='request'>Вернуться</a>")
            Request.objects.create(name=name, phone=phone).save()
            request.session["request_submitted"] = True
            return redirect("MainApp:sucess")

def requests(request):
    if request.user.is_superuser:
        requests = Request.objects.all().order_by("-datetime")
        return render(request, "requests.html", context={"requests": requests})
    HttpResponseNotFound("Для админа")

