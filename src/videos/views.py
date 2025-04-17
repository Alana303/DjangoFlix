from django.shortcuts import render
from playlists.models import Playlist  # Adjust if using another model

def home_view(request):
    qs = Playlist.objects.all()[:6]
    return render(request, "home.html", {"object_list": qs})

def search_view(request):
    query = request.GET.get("q")
    qs = Playlist.objects.filter(title__icontains=query)
    return render(request, "search.html", {"object_list": qs, "query": query})
