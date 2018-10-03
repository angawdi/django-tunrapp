from django.shortcuts import render
from .models import Artist

# Create your views here.
def artist_list(request):
	artists = Artist.objects.all()
	return render(request, 'artist_list.html', {'artists': artists})