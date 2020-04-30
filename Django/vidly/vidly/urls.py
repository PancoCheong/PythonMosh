"""vidly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
### vidly/urls.py ###
from django.contrib import admin
from django.urls import path, include
from api.models import MovieResource
from . import views

movie_resource = MovieResource()

#from django.urls import include
urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    # Django chop off the movies/ from URL and pass the rest URI to movies app,
    # that's why root of movies app is '' empty string
    path('movies/', include('movies.urls')),
    # return resource_name in models.py ie. movies
    path('api/', include(movie_resource.urls))
]
