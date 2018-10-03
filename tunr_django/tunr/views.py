from django.shortcuts import render
from .models import Artist, Song

# Create your views here.
def artist_list(request):
	artists = Artist.objects.all()
	return render(request, 'artist_list.html', {'artists': artists})

def song_list(request):
	songs = Song.objects.all()
	return render(request, 'song_list.html', {'songs': songs})

def artist_details(request, pk):
	artist = Artist.objects.get(id=pk)
	return render(request, 'artist_details.html', {'artist': artist})