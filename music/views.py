from django.shortcuts import render
from django.http import HttpResponse
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    context = {all_albums: all_albums}
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    return HttpResponse('<h2>details for album id:' + str(album_id))


