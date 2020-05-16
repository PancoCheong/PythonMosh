## movies/views.py ##
# http://127.0.0.1:8000/movies/
#
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
#
from .models import Movie

# Create your views here.
# by convention: index function -- mainpage of the app
#
#
#from django.http import HttpResponse


def index(request):     # http request
    # return HttpResponse("My first Django Response")
    # SELECT * FROM movies_movie
    movies = Movie.objects.all()
    #output = ', '.join([m.title for m in movies])
    #
    # render HTML context
    # dictionary is for passing in data to index.html template (inside templates folder)
    return render(request, 'movies/index.html', {'movies': movies})

    # SELECT * FROM movies_movie WHERE release_year=1984
    # Movie.objects.filter(release_year=1984)
    ##
    # get 1 record
    # Movie.objects.get(id=1)
    #
    #

# from django.http import HttpResponse, Http404
# from django.shortcuts import render, get_object_or_404


def detail(request, movie_id):
    # try:
    #     movie = Movie.objects.get(id=movie_id)
    #     ## movie = Movie.objects.get(pk=movie_id) # primary key, same as id
    #     return render(request, 'movies/detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404()
    # Django has shortcuts for above pattern, HTTP 404 if not found
    # pass the 1st param = Movie Class
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
