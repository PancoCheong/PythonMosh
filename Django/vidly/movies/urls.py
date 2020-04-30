# movies/urls.py
# for URL configuration
#
from django.urls import path
# notice: use relative path to import our views.py
from . import views
#
# movies/     - root of app (empty string)
# movies/1    - detail of individual movie (id = 1)
#
# mapping: path vs reference name of function, no ()
# best practice: give a name of each URL, so that if you change the URL later,
# as all other reference to the name, not the URL itself
#
# movie_id is integer, input char will return 404 page
app_name = 'movies'

urlpatterns = [
    # prefix the name with movies to avoid conflict naming to other app
    # the reference in HTML is {% url 'movies_detail' movie.id %}
    # path('', views.index, name='movies_index'),
    # path('<int:movie_id>', views.detail, name='movies_detail')
    #
    # use app_name, the reference become {% url 'movies:detail' movie.id %}
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')

]
