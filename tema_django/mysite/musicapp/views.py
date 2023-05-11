from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from .models import Song
from .utils import search_youtube


def index(request):
    if request.method == 'POST':
        query = request.POST['query']
        youtube_url = search_youtube(query)
        if youtube_url:
            title, artist = query.split(" - ", 1)
            Song.objects.create(title=title.strip(), artist=artist.strip(), youtube_url=youtube_url)
        return HttpResponseRedirect(request.path_info)

    songs = Song.objects.all()
    context = {'songs': songs}
    return render(request, 'musicapp/index.html', context)


def search(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        youtube_url = search_youtube(query)
        return JsonResponse({"youtube_url": youtube_url})
