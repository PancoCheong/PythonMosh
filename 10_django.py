# 10_django.py
# https://www.djangoproject.com/
#
# google search: popular site by django
# Disqus, Bitbucket, Instagram, Mozilla Firefox, Pinterest, NASA, Onion, Mahalo
# https://ddi-dev.com/blog/programming/top-sites-built-django-framework/
#
# read more later:
# https://docs.djangoproject.com/en/3.0/intro/tutorial01/
#
#  mkdir Django
# cd Django
#
# install Django
# pipenv install django==3.0.5
#
# activate virtual environment
# pipenv shell
# cd Django
#
# check installed version
# python -m django --version
#
### create Django project ###
# django-admin startproject vidly
#
# it creates vidly/vidly folders
# manage.py - perform admin tasks start/stop server, migrate database
# outer vidly folder - container folder of the project (the name doesn't matter to Django, you can rename it any time)
# inner vidly folder - it is a package of the project, contain __init__.py
#
# settings.py   - configuration of the project
# urls.py       - defines all endpoints of the application (read more: URL dispatcher)
# wsgi.py       - web server gateway interface, An entry-point for WSGI-compatible web servers to serve your project.
# asgi.py (new in 3.0) - Asynchronous Server Gateway Interface, An entry-point for ASGI-compatible web servers to serve your project.
#
# inside vidly container folder
# python .\manage.py runserver
#
# browser open http://127.0.0.1:8000/
# see the page because of DEBUG = True in settings.py
#
# Ctrl + C to stop
#
# change port
# python .\manage.py runserver 8899
#
# Django projects has multiple apps for each functional area (eg. customer service, orders, shipping etc)
#
# create movies in our example
# provides list of movies and the detail of each movies
#
# Ctrl + C
### create app ###
# python manage.py startapp movies
#
# migrations folder - for data migration
# admin.py - define admin area for managing the movies
# apps.py - configuration for this app
# models.py - represents domain (eg. movie, genre) of this app
# tests.py - automated test
# views.py - take HTTP request and return the response (HTML, json, XML, image etc)
#
#   MVC         vs      Django
# ----------         ----------
# Model         --      Model
# View          --      Template
# Controller    --      View
#
### edit movies/views.py ###
# step 1: define function
#
# def index(request):     # http request
#     return HttpResponse("My first Django Response")
#
# step 2: URL configuration
# create new urls.py file in movies folder and map the URL
# movies/urls.py
#
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.index, name='index')
# ]
#
# step 3: let Django main app to aware of movies app
# update vidly/urls.py
#
# from django.contrib import admin
# from django.urls import path, include
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('movies/', include('movies.urls'))
# ]
#
### browser open ###
# http://127.0.0.1:8000/            # output:Page not found (404)
# http://127.0.0.1:8000/movies/     # output:My first Django Response
#
#
### model ###
# step 1: define model
# movies/models.py
# movies/models.py
# from django.db import models

# Django Model handles how to save data in database


# class Genre(models.Model):
#     name = models.CharField(max_length=255)
#     # models.BooleanField, models.IntegerField, models.FloatField


# class Movie(models.Model):
#     title = models.CharField(max_length=255)
#     release_year = models.IntegerField()
#     number_in_stock = models.IntegerField()
#     daily_rate = models.FloatField()
#     # define relationship with other model
#     genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
#
#
### migration - update database ###
## Django created db.sqlite3 file - for dev or mobile, but no security and concurrency features##
# use MySQL, MS SQL, Oracle and Postgresql for production
#
# download DB Browser for SQLite
# http://www.sqlitebrowser.org/
#
#
# step 2: register model to main app
# vidly/settings.py
#
# Application definition

# INSTALLED_APPS = [
#     'django.contrib.admin',             # admin panel
#     'django.contrib.auth',              # authentication and permission
#     'django.contrib.contenttypes',      # creating generic class within model class
#     'django.contrib.sessions',          # store temp data in current session
#     'django.contrib.messages',          # dispay message to user
#     'django.contrib.staticfiles',       # manage files like css and image
#     # check movies/apps.py, it has MoviesConfig class
#     'movies.apps.MoviesConfig'
# ]
#
# # Migrate Models to Database (just like code first)
# step 3: create migration file
# python manage.py makemigrations
#
# output:movies\migrations\0001_initial.py
#
# Django auto create ID field with auto increment
#
# step 4: run the migration
# python manage.py runserver  # show pending migration warning
#
# python manage.py migrate
#
# output:
# Running migrations:
#   Applying contenttypes.0001_initial... OK
#   Applying auth.0001_initial... OK
#   Applying admin.0001_initial... OK
#   Applying admin.0002_logentry_remove_auto_add... OK
#   Applying admin.0003_logentry_add_action_flag_choices... OK
#   Applying contenttypes.0002_remove_content_type_name... OK
#   Applying auth.0002_alter_permission_name_max_length... OK
#   Applying auth.0003_alter_user_email_max_length... OK
#   Applying auth.0004_alter_user_username_opts... OK
#   Applying auth.0005_alter_user_last_login_null... OK
#   Applying auth.0006_require_contenttypes_0002... OK
#   Applying auth.0007_alter_validators_add_error_messages... OK
#   Applying auth.0008_alter_user_username_max_length... OK
#   Applying auth.0009_alter_user_last_name_max_length... OK
#   Applying auth.0010_alter_group_name_max_length... OK
#   Applying auth.0011_update_proxy_permissions... OK
#   Applying movies.0001_initial... OK
#   Applying sessions.0001_initial... OK
#
# 13 tables are created, prefix by app_
#   11 tables by Django,
#   2 for movies: movies_movie, movies_genre
#
# django_migrations - keep track of migration
#
#
### update the model ###
# add date_created field
# movies/models.py
# pass reference to method, no ()
# if use timezone.now(), the value is fixed date value of this moment in time.
# date_created = models.DateTimeField(default=timezone.now)
#
# python manage.py makemigrations
# python manage.py migrate
#
# never delete migration files as Python apply them in sequence
#
#
### see the SQL statement of migration ###
# python manage.py sqlmigrate movies 0001
#
#
#
### admin ###
## Django come with admin panel for your project ##
# http://127.0.0.1:8000/admin
#
# create super user (no need to kill running server)
# python manage.py createsuperuser
#
# input username, email and password
#
# the first page load is slow
#
# by default, it can only manage the users and groups
# you can bring the models to admin panel to manage
#
# movies/admin.py
# from django.contrib import admin
# from .models import Genre, Movie

# # Register your models here.
# admin.site.register(Genre)
# admin.site.register(Movie)
#
# use DB Browser for SQLite to create a record in movies_genre table
# id=1, name="Action"
#
# browser, refresh the page, click GENRE table
# GENRE
# Genre object (1)      # it shows Genre object (id number), which is not user friendly
# reason: default representation of a genre object as string (ie. __str__ method)
#
#
### customized the admin page ###
# default output:Genre object (1)
# override the __str__ method to display the value of name
# movies/models.py
# class Genre(models.Model):
#     name = models.CharField(max_length=255)
#     # models.BooleanField, models.IntegerField, models.FloatField

#     def __str__(self):
#         return self.name
#
#
# customized the Admin page, you need additional class xxxxAdmin
# define the class first, this class is the representation on admin page
#
# override ModelAdmin to display the id field as well
# define GenreAdmin class and register it
#  movies/admin.py
#
# from django.contrib import admin
# from .models import Genre, Movie


# class GenreAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')


# # Register your models here.
# admin.site.register(Genre, GenreAdmin)
# admin.site.register(Movie)
#
#
### add moive in UI ###
# the data attributes that we can override
# class MovieAdmin(admin.ModelAdmin):
# fields = ('title', 'genre')         # defines the fields shown on the form
# single value in tuple, need to add , if not, Python treat it as string with ()
#    exclude = ('date_created',)         # fields that we don't want to show
#    list_display = ('title', 'number_in_stock', 'daily_rate')


# Register your models here.
#admin.site.register(Movie, MovieAdmin)
#
#
#
### Database Abstraction API ###
# models.Model - provide a bunch of methods to interactive with database
# eg. save() method to save data to database, it generates the SQL to perform such action
#
### open movies/views.py ###
#
#
#from .models import Movie


#
# def index(request):     # http request
# return HttpResponse("My first Django Response")
# SELECT * FROM movies_movie
#movies = Movie.objects.all()
#output = ', '.join([m.title for m in movies])
#
# render HTML context
# dictionary is for passing in data to index.html template (inside templates folder)
#output = render(request, 'index.html', {'movies': movies})
# return HttpResponse(output)

# SELECT * FROM movies_movie WHERE release_year=1984
# Movie.objects.filter(release_year=1984)
##
# get 1 record
# Movie.objects.get(id=1)
#
#
# VS code, bottom right -> change Language Mode to HTML
#
# zen coding: generate HTML code in VS Code
# table.table>thead>tr>th*4[TAB key]
# tbody>tr>td*4[TAB key]
#
# Django template tag {% %}
#
# create folder templates
# create index.html
# <h1>Movies</h1>
# <table class="table">
#   <thead>
#     <tr>
#       <th>Title</th>
#       <th>Genre</th>
#       <th>Stock</th>
#       <th>Daily Rate</th>
#     </tr>
#   </thead>
#   <tbody>
#     {% for movie in movies %}
#     <tr>
#       <td>{{ movie.title }}</td>
#       <td>{{movie.genre}}</td>
#       <td>{{movie.number_in_stock}}</td>
#       <td>{{ movie.daily_rate}}</td>
#     </tr>
#     {% endfor %}
#   </tbody>
# </table>
#
#
#
### Bootstrap ###
### https://getbootstrap.com/docs/4.4/getting-started/introduction/#starter-template ###
# reference to cloud css and js file
# or download them
#
### copy the starter template ###
# movies/templates/movies/base.html
# <!DOCTYPE html>
# <html lang="en">
#   <head>
#     <!-- Required meta tags -->
#     <meta charset="utf-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />

#     <!-- Bootstrap CSS -->
#     <link
#       rel="stylesheet"
#       href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
#       integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
#       crossorigin="anonymous"
#     />

#     <title>Vidly</title>
#   </head>
#   <body>
#     {% block content %}

#     {% endblock %}
#     <!-- Optional JavaScript -->
#     <!-- jQuery first, then Popper.js, then Bootstrap JS -->
#     <script
#       src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
#       integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n"
#       crossorigin="anonymous"
#     ></script>
#     <script
#       src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
#       integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
#       crossorigin="anonymous"
#     ></script>
#     <script
#       src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"
#       integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6"
#       crossorigin="anonymous"
#     ></script>
#   </body>
# </html>
#
#
# movies/templates/movies/index.html
# extend base.html and define content block
#
# {% extends 'movies/base.html' %} {% block content %}

# <table class="table">
#   <thead>
#     <tr>
#       <th>Title</th>
#       <th>Genre</th>
#       <th>Stock</th>
#       <th>Daily Rate</th>
#     </tr>
#   </thead>
#   <tbody>
#     {% for movie in movies %}
#     <tr>
#       <td>{{ movie.title }}</td>
#       <td>{{ movie.genre }}</td>
#       <td>{{ movie.number_in_stock }}</td>
#       <td>{{ movie.daily_rate }}</td>
#     </tr>
#     {% endfor %}
#   </tbody>
# </table>
# {% endblock %}
#
##
#
# https://getbootstrap.com/docs/4.4/components/navbar/#brand

# base.html
#   <body>
#     <!-- Navigation Bar -->
#     <nav class="navbar navbar-light bg-light">
#       <a class="navbar-brand" href="#">Vidly</a>
#     </nav>
#     <!-- Main Content inside a container -->
#     <main class="container">
#       {% block content %} {% endblock %}
#     </main>
#
# index.html
# {% extends 'movies/base.html' %} {% block content %}

# <table class="table table-bordered table-hover">
#   <thead>
#
#
#
### sharing a template across multiple apps ###
#
# create templates at root folder #
# copy base.html to it
#
# movies/templates/movies/index.html
# {% extends 'base.html' %} {% block content %}
#
# still cannot find the base.html
#
# Ctrl + P, search settings.py
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],
#         'APP_DIRS': True,
#
#
# detail:
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
urlpatterns = [
    path('', views.index, name='movies_index'),
    path('<int:movie_id>', views.detail, name='movies_detail')
]
